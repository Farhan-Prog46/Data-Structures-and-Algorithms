import pandas as pd
import os
import time
import random
import matplotlib.pyplot as plt

# ============================================================
# LOAD EXCEL -> BUILD 2D ARRAY (TestsConducted Dataset)
# ============================================================

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

missing = []
for c in required_cols:
    if c not in df.columns:
        missing.append(c)

if len(missing) > 0:
    print("ERROR: Missing columns:", missing)
    print("Available columns:", df.columns.tolist())
else:
    df_required = df[required_cols].copy()

    # Clean
    df_required["Date"] = df_required["Date"].astype(str)
    df_required = df_required.fillna(0)

    # Make sure numeric columns are numeric
    df_required["Tested"] = pd.to_numeric(df_required["Tested"], errors="coerce").fillna(0)
    df_required["Positive"] = pd.to_numeric(df_required["Positive"], errors="coerce").fillna(0)
    df_required["Positive/Tested %"] = pd.to_numeric(df_required["Positive/Tested %"], errors="coerce").fillna(0)

    # Convert to 2D array
    data_2d = df_required.values.tolist()

    # Column index map
    col_index = {name: i for i, name in enumerate(required_cols)}

    print("Required columns:", required_cols)
    print("Total rows loaded:", len(data_2d))

    print("\nFirst 10 rows of the final 2D array:")
    for row in data_2d[:10]:
        print(row)

    print("\nLast 10 rows of the final 2D array:")
    for row in data_2d[-10:]:
        print(row)

    # ============================================================
    # Helper: compare values safely (string for Country, float for numeric)
    # ============================================================

    def key_value(row, col):
        if col == col_index["Country"]:
            return str(row[col]).strip().lower()
        else:
            return float(row[col])

    # ============================================================
    # PLOTTING: Top 10 countries by Tested / Positive (GROUPED)
    # ============================================================

    def plot_bar_top10_grouped(rows, title, country_col, value_col, filename):
        totals = {}

        for r in rows:
            country = str(r[col_index[country_col]]).strip()
            value = float(r[col_index[value_col]])
            totals[country] = totals.get(country, 0) + value

        top10 = sorted(totals.items(), key=lambda x: x[1], reverse=True)[:10]

        x = [c for c, _ in top10]
        y = [v for _, v in top10]

        plt.figure()
        plt.bar(x, y)
        plt.title(title)
        plt.xlabel("Country")
        plt.ylabel(value_col)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        out_path = os.path.join(base_dir, filename)
        plt.savefig(out_path)
        plt.close()
        print("Saved graph:", out_path)

    # BEFORE sorting graphs
    plot_bar_top10_grouped(
        data_2d,
        "Top 10 Countries by Tested (Total Tests) - BEFORE Sorting",
        "Country",
        "Tested",
        "bar_tested_before.png"
    )

    plot_bar_top10_grouped(
        data_2d,
        "Top 10 Countries by Positive (Total Positive) - BEFORE Sorting",
        "Country",
        "Positive",
        "bar_positive_before.png"
    )

    # ============================================================
    # SORTING (Insertion, Merge, Quick) - works for string + numeric
    # ============================================================

    def insertion_sort(arr, col):
        data = arr.copy()
        for i in range(1, len(data)):
            key_row = data[i]
            j = i - 1
            while j >= 0 and key_value(data[j], col) > key_value(key_row, col):
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key_row
        return data

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
        left = merge_sort(arr[:mid], col)
        right = merge_sort(arr[mid:], col)
        return merge(left, right, col)

    def quick_sort(arr, col):
        if len(arr) <= 1:
            return arr
        pivot = key_value(arr[len(arr) // 2], col)
        left = [x for x in arr if key_value(x, col) < pivot]
        middle = [x for x in arr if key_value(x, col) == pivot]
        right = [x for x in arr if key_value(x, col) > pivot]
        return quick_sort(left, col) + middle + quick_sort(right, col)

    # Sort by Tested
    SORT_HEADER = "Tested"
    SORT_COL = col_index[SORT_HEADER]

    shuffled = data_2d.copy()
    random.shuffle(shuffled)

    sorted_data = merge_sort(shuffled, SORT_COL)

    print("\nSorted by:", SORT_HEADER)
    print("First 10 rows AFTER sorting:")
    for row in sorted_data[:10]:
        print(row)

    print("\nLast 10 rows AFTER sorting:")
    for row in sorted_data[-10:]:
        print(row)

    # AFTER sorting graphs
    plot_bar_top10_grouped(
        sorted_data,
        "Top 10 Countries by Tested (Total Tests) - AFTER Sorting",
        "Country",
        "Tested",
        "bar_tested_after.png"
    )

    plot_bar_top10_grouped(
        sorted_data,
        "Top 10 Countries by Positive (Total Positive) - AFTER Sorting",
        "Country",
        "Positive",
        "bar_positive_after.png"
    )

    # ============================================================
    # TIMING COMPARISON GRAPH
    # ============================================================

    def time_algorithm(func, arr, col):
        start = time.time()
        func(arr, col)
        end = time.time()
        return end - start

    sizes = [50, 100, 200, 400, 800, min(1000, len(data_2d))]

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

    print("\nTiming Results (seconds):")
    for i in range(len(sizes)):
        print(f"n={sizes[i]} | insertion={insertion_times[i]:.6f} | merge={merge_times[i]:.6f} | quick={quick_times[i]:.6f}")

    plt.figure()
    plt.plot(sizes, insertion_times, marker="o", label="Insertion Sort")
    plt.plot(sizes, merge_times, marker="o", label="Merge Sort")
    plt.plot(sizes, quick_times, marker="o", label="Quick Sort")
    plt.title(f"Sorting Time Comparison (sorted by {SORT_HEADER})")
    plt.xlabel("Input size (n rows)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    out_path = os.path.join(base_dir, "sorting_time_comparison.png")
    plt.savefig(out_path)
    plt.close()
    print("Saved graph:", out_path)

    # ============================================================
    # SEARCHING (Linear + Binary) on two columns: Country + Tested
    # ============================================================

    def linear_search(arr, col, target):
        if col == col_index["Country"]:
            target_key = str(target).strip().lower()
            for i in range(len(arr)):
                if str(arr[i][col]).strip().lower() == target_key:
                    return i
        else:
            target_val = float(target)
            for i in range(len(arr)):
                if float(arr[i][col]) == target_val:
                    return i
        return -1

    def binary_search(arr_sorted, col, target):
        low = 0
        high = len(arr_sorted) - 1

        if col == col_index["Country"]:
            target_key = str(target).strip().lower()
        else:
            target_key = float(target)

        while low <= high:
            mid = (low + high) // 2
            mid_val = key_value(arr_sorted[mid], col)

            if mid_val == target_key:
                return mid
            elif mid_val < target_key:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def binary_search_by_column(arr, col, target):
        arr_sorted = merge_sort(arr.copy(), col)
        idx = binary_search(arr_sorted, col, target)
        return idx, arr_sorted

    # Success + fail examples
    country_success = data_2d[0][col_index["Country"]]
    country_fail = "ZZZ_NOT_REAL"

    tested_success = float(data_2d[0][col_index["Tested"]])
    tested_fail = 999999999999.0

    print("\n=== SEARCHING RESULTS ===")

    print("\n--- LINEAR SEARCH ---")
    idx = linear_search(data_2d, col_index["Country"], country_success)
    print("Linear SUCCESS (Country):", idx)

    idx = linear_search(data_2d, col_index["Country"], country_fail)
    print("Linear FAIL (Country):", idx)

    idx = linear_search(data_2d, col_index["Tested"], tested_success)
    print("Linear SUCCESS (Tested):", idx)

    idx = linear_search(data_2d, col_index["Tested"], tested_fail)
    print("Linear FAIL (Tested):", idx)

    print("\n--- BINARY SEARCH ---")
    idx, _ = binary_search_by_column(data_2d, col_index["Country"], country_success)
    print("Binary SUCCESS (Country):", idx)

    idx, _ = binary_search_by_column(data_2d, col_index["Country"], country_fail)
    print("Binary FAIL (Country):", idx)

    idx, _ = binary_search_by_column(data_2d, col_index["Tested"], tested_success)
    print("Binary SUCCESS (Tested):", idx)

    idx, _ = binary_search_by_column(data_2d, col_index["Tested"], tested_fail)
    print("Binary FAIL (Tested):", idx)
