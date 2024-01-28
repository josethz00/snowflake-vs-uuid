package main

import (
	"time"

	"github.com/fatih/color"
)

func main() {
	boldPurple := color.New(color.FgHiMagenta, color.Bold)
	boldPurple.Println("BENCHMARK: Snowflake vs UUID")
	time.Sleep(800 * time.Millisecond)
	boldPurple.Println(".....................................")
	time.Sleep(1000 * time.Millisecond)
	boldPurple.Println("=====================================")
	time.Sleep(600 * time.Millisecond)
	boldPurple.Println("=====================================")
	time.Sleep(200 * time.Millisecond)
	boldPurple.Println(".....................................")
}
