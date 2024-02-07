import pandas as pd
import os
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

    
snowflake_ordered_selection_times_ms = []

# for each file in dir, read CSV and get elapsed time for ordered selection
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark', f))
        snowflake_ordered_selection_times_ms.append(df.loc[df["Operation"] == "Ordered Selection"]["ElapsedTime"].values[0])


uuid_ordered_selection_times_ms = []

# for each file in dir, read CSV and get elapsed time for ordered selection
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark', f))
        uuid_ordered_selection_times_ms.append(df.loc[df["Operation"] == "Ordered Selection"]["ElapsedTime"].values[0])

print("ORDERED SELECTION (SNOWFLAKE)")
print(f"Mean: {np.mean(snowflake_ordered_selection_times_ms)}")
print(f"Median: {np.median(snowflake_ordered_selection_times_ms)}")
print(f"Standard deviation: {np.std(snowflake_ordered_selection_times_ms)}")
print(f"Variance: {np.var(snowflake_ordered_selection_times_ms)}")

print("ORDERED SELECTION (UUID)")
print(f"Mean: {np.mean(uuid_ordered_selection_times_ms)}")
print(f"Median: {np.median(uuid_ordered_selection_times_ms)}")
print(f"Standard deviation: {np.std(uuid_ordered_selection_times_ms)}")
print(f"Variance: {np.var(uuid_ordered_selection_times_ms)}")

print("T-TEST - ORDERED SELECTION")
print(stats.ttest_ind(snowflake_ordered_selection_times_ms, uuid_ordered_selection_times_ms, equal_var=False))
print("\n =================================== \n")


snowflake_generation_times_ms = []

# for each file in dir, read CSV and get elapsed time for id generation
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark', f))
        snowflake_generation_times_ms.append(df.loc[df["Operation"] == "Generation"]["ElapsedTime"].values[0])

uuid_generation_times_ms = []

# for each file in dir, read CSV and get elapsed time for id generation
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark', f))
        uuid_generation_times_ms.append(df.loc[df["Operation"] == "Generation"]["ElapsedTime"].values[0])

print("ID GENERATION (SNOWFLAKE)")
print(f"Mean: {np.mean(snowflake_generation_times_ms)}")
print(f"Median: {np.median(snowflake_generation_times_ms)}")
print(f"Standard deviation: {np.std(snowflake_generation_times_ms)}")
print(f"Variance: {np.var(snowflake_generation_times_ms)}")

print("ID GENERATION (UUID)")
print(f"Mean: {np.mean(uuid_generation_times_ms)}")
print(f"Median: {np.median(uuid_generation_times_ms)}")
print(f"Standard deviation: {np.std(uuid_generation_times_ms)}")
print(f"Variance: {np.var(uuid_generation_times_ms)}")

print("T-TEST - ID GENERATION")
print(stats.ttest_ind(snowflake_generation_times_ms, uuid_generation_times_ms, equal_var=False))
print("\n =================================== \n")


snowflake_insertion_times_ms = []

# for each file in dir, read CSV and get elapsed time for insertion
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark', f))
        snowflake_insertion_times_ms.append(df.loc[df["Operation"] == "Generation + Insertion"]["ElapsedTime"].values[0])

uuid_insertion_times_ms = []

# for each file in dir, read CSV and get elapsed time for insertion
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark', f))
        uuid_insertion_times_ms.append(df.loc[df["Operation"] == "Generation + Insertion"]["ElapsedTime"].values[0])

print("INSERTION (SNOWFLAKE)")
print(f"Mean: {np.mean(snowflake_insertion_times_ms)}")
print(f"Median: {np.median(snowflake_insertion_times_ms)}")
print(f"Standard deviation: {np.std(snowflake_insertion_times_ms)}")
print(f"Variance: {np.var(snowflake_insertion_times_ms)}")

print("INSERTION (UUID)")
print(f"Mean: {np.mean(uuid_insertion_times_ms)}")
print(f"Median: {np.median(uuid_insertion_times_ms)}")
print(f"Standard deviation: {np.std(uuid_insertion_times_ms)}")
print(f"Variance: {np.var(uuid_insertion_times_ms)}")

print("T-TEST - INSERTION")
print(stats.ttest_ind(snowflake_insertion_times_ms, uuid_insertion_times_ms, equal_var=False))
print("\n =================================== \n")


snowflake_selection_times_ms = []

# for each file in dir, read CSV and get elapsed time for selection
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark', f))
        snowflake_selection_times_ms.append(df.loc[df["Operation"] == "Selection"]["ElapsedTime"].values[0])

uuid_selection_times_ms = []

# for each file in dir, read CSV and get elapsed time for selection
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark', f))
        uuid_selection_times_ms.append(df.loc[df["Operation"] == "Selection"]["ElapsedTime"].values[0])

print("SELECTION (SNOWFLAKE)")
print(f"Mean: {np.mean(snowflake_selection_times_ms)}")
print(f"Median: {np.median(snowflake_selection_times_ms)}")
print(f"Standard deviation: {np.std(snowflake_selection_times_ms)}")
print(f"Variance: {np.var(snowflake_selection_times_ms)}")

print("SELECTION (UUID)")
print(f"Mean: {np.mean(uuid_selection_times_ms)}")
print(f"Median: {np.median(uuid_selection_times_ms)}")
print(f"Standard deviation: {np.std(uuid_selection_times_ms)}")
print(f"Variance: {np.var(uuid_selection_times_ms)}")

print("T-TEST - SELECTION")
print(stats.ttest_ind(snowflake_selection_times_ms, uuid_selection_times_ms, equal_var=False))
print("\n =================================== \n")


snowflake_update_times_ms = []

# for each file in dir, read CSV and get elapsed time for update
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark', f))
        snowflake_update_times_ms.append(df.loc[df["Operation"] == "Update"]["ElapsedTime"].values[0])

uuid_update_times_ms = []

# for each file in dir, read CSV and get elapsed time for update
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark', f))
        uuid_update_times_ms.append(df.loc[df["Operation"] == "Update"]["ElapsedTime"].values[0])

print("UPDATE (SNOWFLAKE)")
print(f"Mean: {np.mean(snowflake_update_times_ms)}")
print(f"Median: {np.median(snowflake_update_times_ms)}")
print(f"Standard deviation: {np.std(snowflake_update_times_ms)}")
print(f"Variance: {np.var(snowflake_update_times_ms)}")

print("UPDATE (UUID)")
print(f"Mean: {np.mean(uuid_update_times_ms)}")
print(f"Median: {np.median(uuid_update_times_ms)}")
print(f"Standard deviation: {np.std(uuid_update_times_ms)}")
print(f"Variance: {np.var(uuid_update_times_ms)}")

print("T-TEST - UPDATE")
print(stats.ttest_ind(snowflake_update_times_ms, uuid_update_times_ms, equal_var=False))
print("\n =================================== \n")


snowflake_search_by_id_times_ms = []

# for each file in dir, read CSV and get elapsed time for search by id
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark', f))
        snowflake_search_by_id_times_ms.append(df.loc[df["Operation"] == "Search"]["ElapsedTime"].values[0])

uuid_search_by_id_times_ms = []

# for each file in dir, read CSV and get elapsed time for search by id
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark', f))
        uuid_search_by_id_times_ms.append(df.loc[df["Operation"] == "Search"]["ElapsedTime"].values[0])

print("SEARCH BY ID (SNOWFLAKE)")
print(f"Mean: {np.mean(snowflake_search_by_id_times_ms)}")
print(f"Median: {np.median(snowflake_search_by_id_times_ms)}")
print(f"Standard deviation: {np.std(snowflake_search_by_id_times_ms)}")
print(f"Variance: {np.var(snowflake_search_by_id_times_ms)}")

print("SEARCH BY ID (UUID)")
print(f"Mean: {np.mean(uuid_search_by_id_times_ms)}")
print(f"Median: {np.median(uuid_search_by_id_times_ms)}")
print(f"Standard deviation: {np.std(uuid_search_by_id_times_ms)}")
print(f"Variance: {np.var(uuid_search_by_id_times_ms)}")

print("T-TEST - SEARCH BY ID")
print(stats.ttest_ind(snowflake_search_by_id_times_ms, uuid_search_by_id_times_ms, equal_var=False))
print("\n =================================== \n")


plt.figure(figsize=(10, 6))

plt.plot(snowflake_ordered_selection_times_ms, label="Snowflake", marker='o', linestyle='-', linewidth=2, markersize=5)
plt.plot(uuid_ordered_selection_times_ms, label="UUID", marker='s', linestyle='--', linewidth=2, markersize=5)

plt.xlabel('Benchmark Iteration')
plt.ylabel('Time (ms)')
plt.title("Ordered Selection: Performance Comparison")
plt.legend(loc='upper right')

plt.grid(True)


plt.savefig("ordered_selection_improved.png", dpi=300)
plt.show()


plt.figure(figsize=(10, 6))

plt.plot(snowflake_selection_times_ms, label="Snowflake", marker='o', linestyle='-', linewidth=2, markersize=5)
plt.plot(uuid_selection_times_ms, label="UUID", marker='s', linestyle='--', linewidth=2, markersize=5)

plt.xlabel('Benchmark Iteration')
plt.ylabel('Time (ms)')
plt.title("Selection: Performance Comparison")
plt.legend(loc='upper right')

plt.grid(True)


plt.savefig("selection_improved.png", dpi=300)
plt.show()


plt.figure(figsize=(10, 6))

plt.plot(snowflake_update_times_ms, label="Snowflake", marker='o', linestyle='-', linewidth=2, markersize=5)
plt.plot(uuid_update_times_ms, label="UUID", marker='s', linestyle='--', linewidth=2, markersize=5)

plt.xlabel('Benchmark Iteration')
plt.ylabel('Time (ms)')
plt.title("Update: Performance Comparison")
plt.legend(loc='upper right')

plt.grid(True)


plt.savefig("update_improved.png", dpi=300)
plt.show()


plt.figure(figsize=(10, 6))

plt.plot(snowflake_search_by_id_times_ms, label="Snowflake", marker='o', linestyle='-', linewidth=2, markersize=5)
plt.plot(uuid_search_by_id_times_ms, label="UUID", marker='s', linestyle='--', linewidth=2, markersize=5)

plt.xlabel('Benchmark Iteration')
plt.ylabel('Time (ms)')
plt.title("Search by ID: Performance Comparison")
plt.legend(loc='upper right')

plt.grid(True)


plt.savefig("search_improved.png", dpi=300)
plt.show()


plt.figure(figsize=(10, 6))

plt.plot(snowflake_generation_times_ms, label="Snowflake", marker='o', linestyle='-', linewidth=2, markersize=5)
plt.plot(uuid_generation_times_ms, label="UUID", marker='s', linestyle='--', linewidth=2, markersize=5)

plt.xlabel('Benchmark Iteration')
plt.ylabel('Time (ms)')
plt.title("ID Generation: Performance Comparison")
plt.legend(loc='upper right')

plt.grid(True)


plt.savefig("idgeneration_improved.png", dpi=300)
plt.show()


plt.figure(figsize=(10, 6))

plt.plot(snowflake_insertion_times_ms, label="Snowflake", marker='o', linestyle='-', linewidth=2, markersize=5)
plt.plot(uuid_insertion_times_ms, label="UUID", marker='s', linestyle='--', linewidth=2, markersize=5)

plt.xlabel('Benchmark Iteration')
plt.ylabel('Time (ms)')
plt.title("Insertion: Performance Comparison")
plt.legend(loc='upper right')

plt.grid(True)


plt.savefig("insertion_improved.png", dpi=300)
plt.show()