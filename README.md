# Snowflake vs UUID

This is a simple benchmark to compare the performance of Snowflake and UUID.
It was built with Go + Docker + SQLx + PostgreSQL. The data collected was used to generate the graphs below.

The graphs and the data analysis were made with Python3, so please check if you have it installed on your machine.

<img src="https://github.com/josethz00/snowflake-vs-uuid/blob/main/images/benchmark_comparison.png?raw=True" />

## How to run

1. Install Go
2. Install Docker
3. Install Python3
4. Run the following commands:

```bash
docker-compose up -d
```

and then, run the Snowflake benchmark:

```bash
./run-snowflake.sh
```

or the UUID benchmark:

```bash
./run-uuid.sh
```

## How to analyze the data

After running the benchmarks, you can analyze the data by running the following command:

```bash
python3 benchmark_analysis.py
```

this will generate the graphs and print the data analysis. The generated graphs will be saved in the `images` folder. And the data from the benchmarks will be saved in the `reports` folder.

## Results

### ID Generation

<img src="https://github.com/josethz00/snowflake-vs-uuid/blob/main/images/idgeneration.png?raw=True" />

### ID Insertion

<img src="https://github.com/josethz00/snowflake-vs-uuid/blob/main/images/insertion.png?raw=True" />

### ID Selection

<img src="https://github.com/josethz00/snowflake-vs-uuid/blob/main/images/selection.png?raw=True" />

### ID Search (WHERE)

<img src="https://github.com/josethz00/snowflake-vs-uuid/blob/main/images/search.png?raw=True" />

### Ordered Selection (SELECT + ORDER BY)

<img src="https://github.com/josethz00/snowflake-vs-uuid/blob/main/images/ordered_selection_improved.png?raw=True" />

### Update

<img src="https://github.com/josethz00/snowflake-vs-uuid/blob/main/images/update.png?raw=True" />

## Validating Results

The results were validated by running the benchmarks multiple times (30), calculating the average and the standard deviation, and running a t-test to compare the means of the two groups. The t-test was performed with a 95% confidence level.

<img src="https://github.com/josethz00/snowflake-vs-uuid/blob/main/images/statistical_significance.png?raw=True" />

## Hardware Used for the benchmark

- DELL Inspiron 5
  - Intel 7 11th Gen
  - 16 GB RAM DDR4
  - 512 GB SSD
  - 2GB dedicated GPU
