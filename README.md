# Snowflake vs UUID

This is a simple benchmark to compare the performance of Snowflake and UUID.
It was built with Go + SQLx + PostgreSQL. The data collected was used to generate the graphs below.

<img src="https://github.com/josethz00/snowflake-vs-uuid/blob/main/images/benchmark_comparison.png?raw=True" />

## How to run

1. Install Go
2. Install Docker
3. Run the following commands:

```bash
docker-compose up -d
```

and then

```bash
go run main.go
```
