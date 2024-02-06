#!/bin/bash

# Number of runs
RUNS=10

# Number of IDs to generate for each run
NUM_IDS=200000

echo "Running benchmark $RUNS times with $NUM_IDS IDs each..."

for i in $(seq 1 $RUNS); do
    echo "Run $i..."
    printf "%d\n" $NUM_IDS | docker exec -i snowflake-benchmark ./snowflakebenchmark.out
done

echo "Benchmark completed."

# create dir if not exists
mkdir -p reports/snowflakebenchmark

docker cp snowflake-benchmark:/app/reports/snowflakebenchmark/  reports/snowflakebenchmark
mv reports/snowflakebenchmark/snowflakebenchmark/* ./reports/snowflakebenchmark
rm -r reports/snowflakebenchmark/snowflakebenchmark
