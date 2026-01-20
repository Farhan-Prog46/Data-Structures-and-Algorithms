# ----------------------------------------
# Course: BTP500
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID: 154714232
# Lab: 02
# ----------------------------------------

import time
import random

# -------- LINEAR SEARCH FUNCTION -------- #
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# -------- TEST FUNCTION -------- #
def test_linear_search(n):
    print("\n--------------------------------------")
    print(f"Testing Linear Search for n = {n}")
    print("--------------------------------------")

    arr = random.sample(range(1, 200), n)

    successful_key = arr[n // 2]
    unsuccessful_key = 999

    # Successful search
    start = time.time()
    success_index = linear_search(arr, successful_key)
    success_time = time.time() - start

    # Unsuccessful search
    start = time.time()
    fail_index = linear_search(arr, unsuccessful_key)
    fail_time = time.time() - start

    # Print results
    print(f"\nSuccessful Search -> Item: {successful_key}, Index: {success_index}, Time: {success_time:.6f}s")
    print(f"Unsuccessful Search -> Item: {unsuccessful_key}, Index: {fail_index}, Time: {fail_time:.6f}s")

    total_time = success_time + fail_time
    print(f"Total Time for Linear Search: {total_time:.6f}s")

# -------- MAIN PROGRAM -------- #
print("======================================")
print("Course Code: BTP500")
print("Student Name: Syed Farhan Zaheer Hussainy")
print("Student ID: 154714232")
print("Lab 02 - Linear Search")
print("======================================")

for size in [10, 20, 30]:
    test_linear_search(size)
