#!/bin/bash

# Number of runs
RUNS=10

# Number of IDs to generate for each run
NUM_IDS=100000

echo "Running benchmark $RUNS times with $NUM_IDS IDs each..."

for i in $(seq 1 $RUNS); do
    echo "Run $i..."
    printf "%d\n" $NUM_IDS | docker exec -i uuid-benchmark ./uuidbenchmark.out
done

echo "Benchmark completed."

# create dir if not exists
mkdir -p reports/uuidbenchmark

docker cp uuid-benchmark:/app/reports/uuidbenchmark/  reports/uuidbenchmark
mv reports/uuidbenchmark/uuidbenchmark/* ./reports/uuidbenchmark
rm -r reports/uuidbenchmark/uuidbenchmark
