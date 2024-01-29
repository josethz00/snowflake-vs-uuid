package main

import (
	"fmt"
	"math/rand"
	"runtime"
	"sync"
	"time"

	"github.com/bwmarrin/snowflake"
	"github.com/fatih/color"
	"github.com/josethz00/snowflake-vs-uuid/utils"
)

func main() {
	rand.Seed(time.Now().Unix())
	boldPurple := color.New(color.FgHiMagenta, color.Bold)
	yellow := color.New(color.FgHiYellow)
	boldPurple.Println("BENCHMARK: Snowflake vs UUID")
	db := utils.NewDB().ConnectDB()
	defer db.TruncateTestsSnowflakeTable()
	defer db.TruncateTestsUUIDTable()

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
	boldCyan.Println("Elapsed time for UUIDs:", elapsedTime)

	yellow.Print("--------------------------------------------------------------------")
	fmt.Println()

	boldCyan.Printf("Generating %d Snowflakes... \n", numIds)
	wg.Add(numGoroutines)
	startTime = time.Now()

	for i := 0; i < numGoroutines; i++ {
		go func(wg *sync.WaitGroup) {
			defer wg.Done()
			for j := 0; j < numIds/numGoroutines; j++ {
				utils.GenSnowflake(snowflakeNode)
			}
		}(&wg)
	}

	wg.Wait()
	elapsedTime = time.Since(startTime)
	boldCyan.Println("Elapsed time for Snowflakes:", elapsedTime)

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
	boldCyan.Println("Elapsed time for UUIDs insertion:", elapsedTime)

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
	boldCyan.Println("Elapsed time for Snowflakes insertion:", elapsedTime)

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
	boldCyan.Println("Elapsed time for UUIDs selection:", elapsedTime)

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
	boldCyan.Println("Elapsed time for Snowflakes selection:", elapsedTime)

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
	boldCyan.Println("Elapsed time for UUID search:", elapsedTime)

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
	boldCyan.Println("Elapsed time for Snowflake search:", elapsedTime)
}
