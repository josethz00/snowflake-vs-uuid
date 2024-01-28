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

	boldCyan := color.New(color.FgHiCyan, color.Bold)

	var wg sync.WaitGroup
	numGoroutines := runtime.GOMAXPROCS(0) // Limit the number of goroutines to the number of CPU cores
	wg.Add(numGoroutines)

	// UUID
	boldCyan.Printf("Generating %d UUIDs... \n", numIds)
	startTime := time.Now()

	for i := 0; i < numGoroutines; i++ {
		go func(wg *sync.WaitGroup) {
			defer wg.Done()
			for j := 0; j < 1000/numGoroutines; j++ {
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
			for j := 0; j < 1000/numGoroutines; j++ {
				utils.GenSnowflake(snowflakeNode)
			}
		}(&wg)
	}

	wg.Wait()
	elapsedTime = time.Since(startTime)
	boldCyan.Println("Elapsed time for Snowflakes:", elapsedTime)
}
