import pandas as pd
import os
import time
import random
import matplotlib.pyplot as plt

# TASK 1 — LOAD EXCEL --------------------------------------------------------------------

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "TestsConducted_AllDates_13July2020.csv.xlsx")

required_cols = [
    "Country",
    "Date",
    "Tested",
    "Positive",
    "Positive/Tested %"
]

df = pd.read_excel(file_path, engine="openpyxl", nrows=1000)

missing = [c for c in required_cols if c not in df.columns]
if missing:
    print("ERROR: Missing columns:", missing)
    print("Available columns:", df.columns.tolist())
    exit()

df = df[required_cols].copy()

# Clean data
df["Date"] = df["Date"].astype(str)
df = df.fillna(0)
df["Tested"] = pd.to_numeric(df["Tested"], errors="coerce").fillna(0)
df["Positive"] = pd.to_numeric(df["Positive"], errors="coerce").fillna(0)
df["Positive/Tested %"] = pd.to_numeric(df["Positive/Tested %"], errors="coerce").fillna(0)

# Convert to 2D array
data_2d = df.values.tolist()
col_index = {name: i for i, name in enumerate(required_cols)}

print("Total rows loaded:", len(data_2d))

print("\nFirst 10 rows:")
for r in data_2d[:10]:
    print(r)

print("\nLast 10 rows:")
for r in data_2d[-10:]:
    print(r)

# HELPER FOR COMPARISON
def key_value(row, col):
    if col == col_index["Country"]:
        return str(row[col]).strip().lower()
    return float(row[col])

# TASK 2 — SORTING ALGORITHMS --------------------------------------------------------------------
# Isertion
def insertion_sort(arr, col):
    data = arr.copy()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key_value(data[j], col) > key_value(key, col):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# merge
def merge(left, right, col):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key_value(left[i], col) <= key_value(right[j], col):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr, col):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(
        merge_sort(arr[:mid], col),
        merge_sort(arr[mid:], col),
        col
    )

# quick sort
def quick_sort(arr, col):
    if len(arr) <= 1:
        return arr
    pivot = key_value(arr[len(arr) // 2], col)
    left = [x for x in arr if key_value(x, col) < pivot]
    middle = [x for x in arr if key_value(x, col) == pivot]
    right = [x for x in arr if key_value(x, col) > pivot]
    return quick_sort(left, col) + middle + quick_sort(right, col)

# PLOTTING FUNCTION
def plot_bar_rows(rows, title, filename):
    x = [str(r[col_index["Country"]]) for r in rows]
    y = [float(r[col_index["Tested"]]) for r in rows]

    plt.figure()
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel("Country")
    plt.ylabel("Tested")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig(os.path.join(base_dir, filename))
    plt.close()
    print("Saved graph:", filename)

# Random sample data to test 
SORT_COL = col_index["Tested"]

sample_10 = data_2d.copy()
random.shuffle(sample_10)
sample_10 = sample_10[:10]

# BEFORE sorting graph
plot_bar_rows(
    sample_10,
    "Same 10 Records by Tested (BEFORE Sorting)",
    "before_testing.png"
)

# AFTER Insertion Sort
sample_insertion = insertion_sort(sample_10, SORT_COL)
plot_bar_rows(
    sample_insertion[::-1],
    "Same 10 Records by Tested (AFTER Insertion Sort)",
    "after_insertion.png"
)

# AFTER Merge Sort
sample_merge = merge_sort(sample_10, SORT_COL)
plot_bar_rows(
    sample_merge[::-1],
    "Same 10 Records by Tested (AFTER Merge Sort)",
    "after_merge.png"
)

# AFTER Quick Sort
sample_quick = quick_sort(sample_10, SORT_COL)
plot_bar_rows(
    sample_quick[::-1],
    "Same 10 Records by Tested (AFTER Quick Sort)",
    "after_quick.png"
)

# TIME COMPARISON

def time_algorithm(func, arr, col):
    start = time.time()
    func(arr, col)
    return time.time() - start

sizes = [50, 100, 200, 400, 800, min(1000, len(data_2d))] # size of data used to compare time taken by algorithms

insertion_times = []
merge_times = []
quick_times = []

for s in sizes:
    subset = data_2d[:s].copy()
    random.shuffle(subset)
    insertion_times.append(time_algorithm(insertion_sort, subset, SORT_COL))

    subset = data_2d[:s].copy()
    random.shuffle(subset)
    merge_times.append(time_algorithm(merge_sort, subset, SORT_COL))

    subset = data_2d[:s].copy()
    random.shuffle(subset)
    quick_times.append(time_algorithm(quick_sort, subset, SORT_COL))

# DISPLAY TIMINGS

print("\nTiming Results (seconds):")
for i in range(len(sizes)):
    print(
        f"n={sizes[i]:<4} | "
        f"insertion={insertion_times[i]:.6f} | "
        f"merge={merge_times[i]:.6f} | "
        f"quick={quick_times[i]:.6f}"
    )

# bar graph for time comparison
n_index = sizes.index(max(sizes))

plt.figure()
plt.bar(
    ["Insertion", "Merge", "Quick"],
    [
        insertion_times[n_index],
        merge_times[n_index],
        quick_times[n_index]
    ]
)

plt.yscale("log")   
plt.title(f"Sorting Time Comparison for n = {sizes[n_index]} (Log Scale)")
plt.xlabel("Sorting Algorithm")
plt.ylabel("Time (seconds, log scale)")
plt.tight_layout()
plt.savefig(os.path.join(base_dir, "sorting_time_bar_comparison_log.png"))
plt.close()


# TASK 3 — SEARCHING (LINEAR & BINARY) --------------------------------------------------------------------

def linear_search(arr, col, target):
    for i in range(len(arr)):
        if float(arr[i][col]) == float(target):
            return i
    return -1

def binary_search(arr, col, target):
    low, high = 0, len(arr) - 1
    target = float(target)

    while low <= high:
        mid = (low + high) // 2
        if float(arr[mid][col]) == target:
            return mid
        elif float(arr[mid][col]) < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# DISPLAY SEARCH RESULTS
print("\nSEARCH RESULTS")
sorted_full = merge_sort(data_2d.copy(), SORT_COL)

success_val = sorted_full[-1][SORT_COL]
fail_val = -1

print("Linear SUCCESS:", linear_search(data_2d, SORT_COL, success_val))
print("Linear FAIL:", linear_search(data_2d, SORT_COL, fail_val))
print("Binary SUCCESS:", binary_search(sorted_full, SORT_COL, success_val))
print("Binary FAIL:", binary_search(sorted_full, SORT_COL, fail_val))
