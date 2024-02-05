#!/bin/bash

# Number of runs
RUNS=10

# Number of IDs to generate for each run
NUM_IDS=100000

echo "Running benchmark $RUNS times with $NUM_IDS IDs each..."

for i in $(seq 1 $RUNS); do
    echo "Run $i..."
    printf "%d\n" $NUM_IDS | docker exec -i snowflake-benchmark ./snowflakebenchmark.out
done

echo "Benchmark completed."
