import pandas as pd
import os

# Get the folder where this .py file is located
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "by-age-excel.xlsx")

# Read Excel
df = pd.read_excel(file_path, engine="openpyxl", nrows=1000)

# Choose required columns 
required_cols = [
    "date",
    "location_key",
    "new_confirmed_age_0",
    "cumulative_confirmed_age_0",
    "new_deceased_age_0",
    "cumulative_deceased_age_0",
]

# Check missing columns
missing = []
for c in required_cols:
    if c not in df.columns:
        missing.append(c)

if len(missing) > 0:
    print("ERROR: These columns are missing in the Excel file:", missing)
    print("Available columns are:", df.columns.tolist())
else:
    # Keep only the required columns
    df_required = df[required_cols].copy()

    # Make the date consistent (string format)
    df_required["date"] = df_required["date"].astype(str)

    # Replace NaN with 0 to make output cleaner
    df_required = df_required.fillna(0)

    # Convert to 2D array (list of lists)
    data_2d = df_required.values.tolist()

    
    print("Required columns:", required_cols)
    print("Total rows loaded:", len(data_2d))

    print("\nFirst 10 rows of the final 2D array:")
    for row in data_2d[:10]:
        print(row)

    print("\nLast 10 rows of the final 2D array:")
    for row in data_2d[-10:]:
        print(row)

#----------------------------------------------------------------
# TASK 2 — SORTING 

SORT_COL = col_index["cumulative_confirmed_age_0"]

# Insertion Sort
def insertion_sort(arr, col):
    data = arr.copy()
    for i in range(1, len(data)):
        curr = data[i]
        j = i
        while j > 0 and data[j - 1][col] > curr[col]:
            data[j] = data[j - 1]
            j -= 1
        data[j] = curr
    return data

# Merge Sort
def merge(left, right, col):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][col] <= right[j][col]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(data, col):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid], col)
    right = merge_sort(data[mid:], col)
    return merge(left, right, col)
