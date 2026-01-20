# ----------------------------------------
# Course: BTP500
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID: 154714232
# Lab: 02
# ----------------------------------------

import time
import random

def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        key = i
        for j in range(i + 1, n):
            if arr[j] < arr[key]:
                key = j
        arr[i], arr[key] = arr[key], arr[i]
    return arr

def test_selection_sort(n):
    print(f"Testing Selection Sort for n = {n}")

    arr = [random.randint(1, 1000) for _ in range(n)]

    start = time.time()
    selection_sort(arr)
    elapsed_time = time.time() - start

    print(f"Selection Sort Time: {elapsed_time:.6f} seconds")
    print("--------------------------------------\n")


print("======================================")
print("Course Code: BTP500")
print("Student Name: Syed Farhan Zaheer Hussainy")
print("Student ID: 154714232")
print("Lab 02 - Selection Sorting")
print("======================================")

# ================================
# Test Cases
# ================================
test_selection_sort(100)
test_selection_sort(200)
test_selection_sort(300)

    