import pandas as pd
import os
import re
import numpy as np
from scipy import stats

def convert_to_miliseconds(time_str: str) -> float:
    match = re.match(r"([0-9.]+)(ms|µs|s)", time_str)
    if not match:
        raise ValueError("Invalid time format")
    
    value, unit = match.groups()
    value = float(value)
    
    if unit == "ms":
        return value  # already in milliseconds
    elif unit == "µs":
        return value / 1000  # convert to milliseconds
    elif unit == "s":
        return value  * 1000  # convert to milliseconds
    else:
        raise ValueError("Unsupported time unit")
    
snowflake_ordered_selection_times_s = []

# for each file in dir, read CSV and get elapsed time for ordered selection
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'snowflakebenchmark', f))
        snowflake_ordered_selection_times_s.append(convert_to_miliseconds(df.loc[df["Operation"] == "Ordered Selection"]["ElapsedTime"].values[0]))


uuid_ordered_selection_times_s = []

# for each file in dir, read CSV and get elapsed time for ordered selection
for f in os.listdir(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark')):
    if f.endswith('.csv'):
        df = pd.read_csv(os.path.join(os.getcwd(), 'reports', 'uuidbenchmark', f))
        uuid_ordered_selection_times_s.append(convert_to_miliseconds(df.loc[df["Operation"] == "Ordered Selection"]["ElapsedTime"].values[0]))

print(snowflake_ordered_selection_times_s)
print(f"Mean: {np.mean(snowflake_ordered_selection_times_s)}")
print(f"Median: {np.median(snowflake_ordered_selection_times_s)}")
print(f"Standard deviation: {np.std(snowflake_ordered_selection_times_s)}")
print(f"Variance: {np.var(snowflake_ordered_selection_times_s)}")

print(uuid_ordered_selection_times_s)
print(f"Mean: {np.mean(uuid_ordered_selection_times_s)}")
print(f"Median: {np.median(uuid_ordered_selection_times_s)}")
print(f"Standard deviation: {np.std(uuid_ordered_selection_times_s)}")
print(f"Variance: {np.var(uuid_ordered_selection_times_s)}")

print(stats.ttest_ind(snowflake_ordered_selection_times_s, uuid_ordered_selection_times_s, equal_var=False).confidence_interval(0.95))