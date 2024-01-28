package main

import (
	"fmt"
	"runtime"
	"sync"
	"time"

	"github.com/bwmarrin/snowflake"
	"github.com/fatih/color"
	"github.com/josethz00/snowflake-vs-uuid/utils"
)

func main() {
	boldPurple := color.New(color.FgHiMagenta, color.Bold)
	boldPurple.Println("BENCHMARK: Snowflake vs UUID")

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
}
