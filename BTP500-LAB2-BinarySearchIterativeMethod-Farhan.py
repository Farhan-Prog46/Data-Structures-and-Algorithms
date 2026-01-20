# ----------------------------------------
# Course: BTP500
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID: 154714232
# Lab: 02
# ----------------------------------------

import time
import random

def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def test_binary_search_iterative(n):
    print("\n--------------------------------------")
    print(f"Testing Binary Search Iterative for n = {n}")
    print("--------------------------------------")

    arr = sorted(random.sample(range(1, 200), n)) 

    successful_key = arr[n // 2]
    unsuccessful_key = 999

    start = time.time()
    success_index = binary_search(arr, successful_key)
    success_time = time.time() - start
    
    start = time.time()
    fail_index = binary_search(arr, unsuccessful_key)
    fail_time = time.time() - start

    print(f"\nSuccessful Search -> Item: {successful_key}, Index: {success_index}, Time: {success_time:.6f}s")
    print(f"Unsuccessful Search -> Item: {unsuccessful_key}, Index: {fail_index}, Time: {fail_time:.6f}s")

    total_time = success_time + fail_time
    print(f"Total Time for Binary Search Iterative: {total_time:.6f}s")


print("======================================")
print("Course Code: BTP500")
print("Student Name: Syed Farhan Zaheer Hussainy")
print("Student ID: 154714232")
print("Lab 02 - Binary Search Iterative")
print("======================================")

# Run test for n=10, 20, 30 automatically
for size in [10, 20, 30]:
    test_binary_search_iterative(size)