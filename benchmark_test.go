package main

import (
	"testing"

	"github.com/bwmarrin/snowflake"
	"github.com/google/uuid"
)

// Benchmark for UUID generation
func BenchmarkUUID(b *testing.B) {
	for i := 0; i < b.N; i++ {
		uuid.New()
	}
}

// Benchmark for Snowflake generation
func BenchmarkSnowflake(b *testing.B) {
	node, err := snowflake.NewNode(1)
	if err != nil {
		b.Fatal("failed to create snowflake node:", err)
	}

	for i := 0; i < b.N; i++ {
		node.Generate()
	}
}
