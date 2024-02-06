import pandas as pd
import os
import re
import numpy as np
from scipy import stats

    
snowflake_ordered_selection_times_s = []

# for each file in dir, read CSV and get elapsed time for ordered selection
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark', f))
        snowflake_ordered_selection_times_s.append(df.loc[df["Operation"] == "Ordered Selection"]["ElapsedTime"].values[0])


uuid_ordered_selection_times_s = []

# for each file in dir, read CSV and get elapsed time for ordered selection
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark', f))
        uuid_ordered_selection_times_s.append(df.loc[df["Operation"] == "Ordered Selection"]["ElapsedTime"].values[0])

print("ORDERED SELECTION (SNOWFLAKE)")
print(f"Mean: {np.mean(snowflake_ordered_selection_times_s)}")
print(f"Median: {np.median(snowflake_ordered_selection_times_s)}")
print(f"Standard deviation: {np.std(snowflake_ordered_selection_times_s)}")
print(f"Variance: {np.var(snowflake_ordered_selection_times_s)}")

print("ORDERED SELECTION (UUID)")
print(f"Mean: {np.mean(uuid_ordered_selection_times_s)}")
print(f"Median: {np.median(uuid_ordered_selection_times_s)}")
print(f"Standard deviation: {np.std(uuid_ordered_selection_times_s)}")
print(f"Variance: {np.var(uuid_ordered_selection_times_s)}")

print("T-TEST - ORDERED SELECTION")
print(stats.ttest_ind(snowflake_ordered_selection_times_s, uuid_ordered_selection_times_s, equal_var=False))
print("\n =================================== \n")


snowflake_generation_times_s = []

# for each file in dir, read CSV and get elapsed time for id generation
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark', f))
        snowflake_generation_times_s.append(df.loc[df["Operation"] == "Generation"]["ElapsedTime"].values[0])

uuid_ordered_generation_times_s = []

# for each file in dir, read CSV and get elapsed time for id generation
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark', f))
        uuid_ordered_generation_times_s.append(df.loc[df["Operation"] == "Generation"]["ElapsedTime"].values[0])

print("ID GENERATION (SNOWFLAKE)")
print(f"Mean: {np.mean(snowflake_generation_times_s)}")
print(f"Median: {np.median(snowflake_generation_times_s)}")
print(f"Standard deviation: {np.std(snowflake_generation_times_s)}")
print(f"Variance: {np.var(snowflake_generation_times_s)}")

print("ID GENERATION (UUID)")
print(f"Mean: {np.mean(uuid_ordered_generation_times_s)}")
print(f"Median: {np.median(uuid_ordered_generation_times_s)}")
print(f"Standard deviation: {np.std(uuid_ordered_generation_times_s)}")
print(f"Variance: {np.var(uuid_ordered_generation_times_s)}")

print("T-TEST - ID GENERATION")
print(stats.ttest_ind(snowflake_generation_times_s, uuid_ordered_generation_times_s, equal_var=False))
print("\n =================================== \n")
