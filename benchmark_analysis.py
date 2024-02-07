from typing import Literal, Optional
import pandas as pd
import os
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker

def read_csv_report_files_by_operation(operation: str, benchmark: Literal["snowflake", "uuid"] = "snowflake", dir: Optional[str] = None) -> list:
    if not dir:
        dir = os.path.join(os.getcwd(), 'reports', f"{benchmark}benchmark")

    times_ms = []

    for f in os.listdir(dir):
        if f.endswith('.csv'):
            df = pd.read_csv(os.path.join(dir, f))
            times_ms.append(df.loc[df["Operation"] == operation]["ElapsedTime"].values[0])

    return times_ms

    
snowflake_ordered_selection_times_ms = read_csv_report_files_by_operation("Ordered Selection", "snowflake")
uuid_ordered_selection_times_ms = read_csv_report_files_by_operation("Ordered Selection", "uuid")

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


snowflake_generation_times_ms = read_csv_report_files_by_operation("Generation", "snowflake")
uuid_generation_times_ms = read_csv_report_files_by_operation("Generation", "uuid")


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


snowflake_insertion_times_ms = read_csv_report_files_by_operation("Generation + Insertion", "snowflake")
uuid_insertion_times_ms = read_csv_report_files_by_operation("Generation + Insertion", "uuid")


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


snowflake_selection_times_ms = read_csv_report_files_by_operation("Selection", "snowflake")
uuid_selection_times_ms = read_csv_report_files_by_operation("Selection", "uuid")


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


snowflake_update_times_ms = read_csv_report_files_by_operation("Update", "snowflake")
uuid_update_times_ms = read_csv_report_files_by_operation("Update", "uuid")


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


snowflake_search_by_id_times_ms = read_csv_report_files_by_operation("Search", "snowflake")
uuid_search_by_id_times_ms = read_csv_report_files_by_operation("Search", "uuid")


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


categories = ("UUID", "Snowflake")
commands_means = {
    'Generation': (np.mean(uuid_generation_times_ms) / 1000, np.mean(snowflake_generation_times_ms) / 1000),
    'INSERT': (np.mean(uuid_insertion_times_ms) /1000, np.mean(snowflake_insertion_times_ms) /1000),
    'SELECT': (np.mean(uuid_selection_times_ms) /1000, np.mean(snowflake_selection_times_ms) /1000),
    'SELECT BY ID (WHERE)': (np.mean(uuid_search_by_id_times_ms) /1000, np.mean(snowflake_search_by_id_times_ms) /1000),
    'SELECT + ORDER BY': (np.mean(uuid_ordered_selection_times_ms) /1000, np.mean(snowflake_ordered_selection_times_ms) /1000),
    'UPDATE': (np.mean(uuid_update_times_ms) /1000, np.mean(snowflake_update_times_ms) /1000),
}


color_palette = plt.get_cmap('tab10')

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10), dpi=100)

plt.subplots_adjust(wspace=0.4, hspace=0.4)

axes = axes.flatten()

for i, (cmd, times) in enumerate(commands_means.items()):
    ax = axes[i]

    x_max = max(times) * 1.2
    ax.set_xlim(0, x_max)

    bars = ax.barh(['UUID', 'Snowflake'], times, color=[color_palette(0), color_palette(1)], height=0.5)

    for bar in bars:
        width = bar.get_width()
        label_x_pos = width if width < x_max / 10 else width - (x_max / 20)
        ax.text(label_x_pos + (bar.get_width() * 0.1), bar.get_y() + bar.get_height()/2, f'{width:.2f} s',
                va='center', ha='left', color='black', fontsize=10, fontweight='bold')

    ax.set_yticks([1, 0])
    ax.set_yticklabels(['UUID', 'Snowflake'])

    ax.set_title(cmd, fontsize=16, fontweight='bold')
    ax.set_xlabel('Time (s)', fontsize=14)

    ax.tick_params(axis='both', which='major', labelsize=12)

    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

fig.tight_layout()
plt.savefig('benchmark_comparison.png', dpi=300, bbox_inches='tight')

plt.show()