package main

import (
	"fmt"
	"math/rand"
	"os"
	"path/filepath"
	"runtime"
	"sync"
	"time"

	"github.com/fatih/color"
	"github.com/josethz00/snowflake-vs-uuid/utils"
)

func main() {
	rand.Seed(42) // fixed seed to reduce variability
	boldPurple := color.New(color.FgHiMagenta, color.Bold)
	yellow := color.New(color.FgHiYellow)
	boldPurple.Println("BENCHMARK: UUID")
	db := utils.NewDB().ConnectDB()
	uuidBenchmarkResults := make(map[string]time.Duration)

	defer db.TruncateTestsUUIDTable()

	var numIds int
	boldPurple.Print("How many IDs do you want to generate?   ")
	fmt.Scanln(&numIds)
	fmt.Print("\n")

	boldCyan := color.New(color.FgHiCyan, color.Bold)

	boldCyan.Print("Warming up ... \n")
	for i := 0; i < 5000; i++ {
		utils.GenUUID()
	}
	for i := 0; i < 5000; i++ {
		uuid := utils.GenUUID()
		db.InsertIntoTestsUUID(uuid, "test")
	}
	_, err := db.SelectIdFromTestsUUID()
	if err != nil {
		panic(err)
	}

	yellow.Print("--------------------------------------------------------------------")

	var wg sync.WaitGroup
	numGoroutines := runtime.GOMAXPROCS(0) // Limit the number of goroutines to the number of CPU cores
	// by passing 0 to GOMAXPROCS we get the number of cores available and doesn't limit
	// the number of goroutines to a lower number
	wg.Add(numGoroutines)

	boldCyan.Printf("Generating %d UUIDs\n", numIds)

	// UUID
	startTime := time.Now()

	for i := 0; i < numGoroutines; i++ {
		// Launch a goroutine for each CPU core
		go func(wg *sync.WaitGroup) {
			defer wg.Done()
			// split the number of IDs to generate between the number of goroutines
			// for example, if we want to generate 1000 IDs and we have 4 goroutines,
			// each goroutine will generate 250 IDs
			for j := 0; j < numIds/numGoroutines; j++ {
				utils.GenUUID()
			}
		}(&wg)
	}

	wg.Wait()
	elapsedTime := time.Since(startTime)
	uuidBenchmarkResults["Generation"] = elapsedTime
	boldCyan.Println("Elapsed time for UUIDs:", elapsedTime)

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()

	// Insert UUIDs into DB
	boldCyan.Printf("Generating %d UUIDs and inserting them into the DB... \n", numIds)
	wg.Add(numGoroutines)
	startTime = time.Now()

	for i := 0; i < numGoroutines; i++ {
		go func(wg *sync.WaitGroup) {
			defer wg.Done()
			for j := 0; j < numIds/numGoroutines; j++ {
				uuid := utils.GenUUID()
				db.InsertIntoTestsUUID(uuid, "test")
			}
		}(&wg)
	}

	wg.Wait()
	elapsedTime = time.Since(startTime)
	uuidBenchmarkResults["Generation + Insertion"] = elapsedTime
	boldCyan.Println("Elapsed time for UUIDs insertion:", elapsedTime)

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()

	// Select UUIDs from DB
	boldCyan.Printf("Selecting %d UUIDs from the DB... \n", numIds)
	startTime = time.Now()

	uuidres, err := db.SelectIdFromTestsUUID()

	if err != nil {
		panic(err)
	}

	elapsedTime = time.Since(startTime)
	uuidBenchmarkResults["Selection"] = elapsedTime
	boldCyan.Println("Elapsed time for UUIDs selection:", elapsedTime)

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()

	// Search By UUID
	boldCyan.Printf("Searching by a unique UUID... \n")
	randomUuidFromResults := uuidres[rand.Intn(len(uuidres))]
	startTime = time.Now()

	_, err = db.SearchByUUID(randomUuidFromResults)

	if err != nil {
		panic(err)
	}

	elapsedTime = time.Since(startTime)
	uuidBenchmarkResults["Search"] = elapsedTime
	boldCyan.Println("Elapsed time for UUID search:", elapsedTime)

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()

	// Select from tests_uuid order by
	boldCyan.Printf("Selecting UUIDs from the DB ordered by id... \n")
	startTime = time.Now()

	_, err = db.OrderedSelectIdFromTestsUUID()

	if err != nil {
		panic(err)
	}

	elapsedTime = time.Since(startTime)
	uuidBenchmarkResults["Ordered Selection"] = elapsedTime
	boldCyan.Println("Elapsed time for UUIDs ordered selection:", elapsedTime)

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()

	// Update record in tests_uuid
	boldCyan.Printf("Updating a record in tests_uuid... \n")
	startTime = time.Now()

	err = db.UpdateTestsUUID(randomUuidFromResults, "test2")

	if err != nil {
		panic(err)
	}

	elapsedTime = time.Since(startTime)
	uuidBenchmarkResults["Update"] = elapsedTime
	boldCyan.Println("Elapsed time for UUID update:", elapsedTime)

	reportsDir := filepath.Join(".", "reports", "uuidbenchmark")

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

	for k, v := range uuidBenchmarkResults {
		_, err = f.WriteString(fmt.Sprintf("%s,%s\n", k, v.String()))
		if err != nil {
			panic(err)
		}
	}

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()
}
