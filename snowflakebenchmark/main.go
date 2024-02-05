package main

import (
	"fmt"
	"math/rand"
	"os"
	"path/filepath"
	"runtime"
	"sync"
	"time"

	"github.com/bwmarrin/snowflake"
	"github.com/fatih/color"
	"github.com/josethz00/snowflake-vs-uuid/utils"
)

func main() {
	rand.Seed(42) // fixed seed to reduce variability
	boldPurple := color.New(color.FgHiMagenta, color.Bold)
	yellow := color.New(color.FgHiYellow)
	boldPurple.Println("BENCHMARK: Snowflake")
	db := utils.NewDB().ConnectDB()
	snowflakeBenchmarkResults := make(map[string]time.Duration)

	defer db.TruncateTestsSnowflakeTable()

	snowflakeNode, err := snowflake.NewNode(1)
	if err != nil {
		panic(err)
	}

	var numIds int
	boldPurple.Print("How many IDs do you want to generate?   ")
	fmt.Scanln(&numIds)
	fmt.Print("\n")

	boldCyan := color.New(color.FgHiCyan, color.Bold)

	var wg sync.WaitGroup
	numGoroutines := runtime.GOMAXPROCS(0) // Limit the number of goroutines to the number of CPU cores
	// by passing 0 to GOMAXPROCS we get the number of cores available and doesn't limit
	// the number of goroutines to a lower number

	boldCyan.Printf("Generating %d Snowflakes... \n", numIds)
	wg.Add(numGoroutines)
	startTime := time.Now()

	for i := 0; i < numGoroutines; i++ {
		go func(wg *sync.WaitGroup) {
			defer wg.Done()
			for j := 0; j < numIds/numGoroutines; j++ {
				utils.GenSnowflake(snowflakeNode)
			}
		}(&wg)
	}

	wg.Wait()
	elapsedTime := time.Since(startTime)
	snowflakeBenchmarkResults["Generation"] = elapsedTime
	boldCyan.Println("Elapsed time for Snowflakes:", elapsedTime)

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()

	// Insert Snowflakes into DB
	boldCyan.Printf("Generating %d Snowflakes and inserting them into the DB... \n", numIds)
	wg.Add(numGoroutines)
	startTime = time.Now()

	for i := 0; i < numGoroutines; i++ {
		go func(wg *sync.WaitGroup) {
			defer wg.Done()
			for j := 0; j < numIds/numGoroutines; j++ {
				snowfid := utils.GenSnowflake(snowflakeNode)
				db.InsertIntoTestsSnowflake(snowfid, "test")
			}
		}(&wg)
	}

	wg.Wait()
	elapsedTime = time.Since(startTime)
	snowflakeBenchmarkResults["Generation + Insertion"] = elapsedTime
	boldCyan.Println("Elapsed time for Snowflakes insertion:", elapsedTime)

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()

	// Select Snowflakes from DB
	boldCyan.Printf("Selecting %d Snowflakes from the DB... \n", numIds)
	startTime = time.Now()

	snowflakeres, err := db.SelectIdFromTestsSnowflake()

	if err != nil {
		panic(err)
	}

	elapsedTime = time.Since(startTime)
	snowflakeBenchmarkResults["Selection"] = elapsedTime
	boldCyan.Println("Elapsed time for Snowflakes selection:", elapsedTime)

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()

	// Search By Snowflake
	boldCyan.Printf("Searching by a unique Snowflake... \n")
	// pick a random snowflake from the results array
	randomSnowflakeFromResults := snowflakeres[rand.Intn(len(snowflakeres))]
	startTime = time.Now()

	_, err = db.SearchBySnowflake(randomSnowflakeFromResults)

	if err != nil {
		panic(err)
	}

	elapsedTime = time.Since(startTime)
	snowflakeBenchmarkResults["Search"] = elapsedTime
	boldCyan.Println("Elapsed time for Snowflake search:", elapsedTime)

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()

	// Select from tests_snowflake order by
	boldCyan.Printf("Selecting Snowflakes from the DB ordered by id... \n")
	startTime = time.Now()

	_, err = db.OrderedSelectIdFromTestsSnowflake()

	if err != nil {
		panic(err)
	}

	elapsedTime = time.Since(startTime)
	snowflakeBenchmarkResults["Ordered Selection"] = elapsedTime
	boldCyan.Println("Elapsed time for Snowflakes ordered selection:", elapsedTime)

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()

	// Update record in tests_snowflake
	boldCyan.Printf("Updating a record in tests_snowflake... \n")
	startTime = time.Now()

	err = db.UpdateTestsSnowflake(randomSnowflakeFromResults, "test2")

	if err != nil {
		panic(err)
	}

	elapsedTime = time.Since(startTime)
	snowflakeBenchmarkResults["Update"] = elapsedTime
	boldCyan.Println("Elapsed time for Snowflake ID single record update:", elapsedTime)

	reportsDir := filepath.Join(".", "reports", "snowflakebenchmark")

	err = os.MkdirAll(reportsDir, os.ModePerm)

	if err != nil {
		panic(err)
	}

	f, err := os.Create(filepath.Join(reportsDir, fmt.Sprintf("results_%d_%d.csv", numIds, time.Now().Unix())))
	if err != nil {
		panic(err)
	}

	defer f.Close()

	_, err = f.WriteString("Operation,ElapsedTime\n")
	if err != nil {
		panic(err)
	}

	for k, v := range snowflakeBenchmarkResults {
		_, err = f.WriteString(fmt.Sprintf("%s,%s\n", k, v.String()))
		if err != nil {
			panic(err)
		}
	}

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()
}
