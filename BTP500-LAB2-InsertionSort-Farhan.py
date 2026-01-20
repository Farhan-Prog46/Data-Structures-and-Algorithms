# ----------------------------------------
# Course: BTP500
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID: 154714232
# Lab: 02
# ----------------------------------------

import time
import random

def insertion_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j > 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
    return arr

def test_insertion_sort(n):
    print(f"Testing Insertion Sort for n = {n}")

    arr = [random.randint(1, 1000) for _ in range(n)]

    start = time.time()
    insertion_sort(arr)
    elapsed_time = time.time() - start

    print(f"Insertion Sort Time: {elapsed_time:.6f} seconds")
    print("--------------------------------------\n")


print("======================================")
print("Course Code: BTP500")
print("Student Name: Syed Farhan Zaheer Hussainy")
print("Student ID: 154714232")
print("Lab 02 - Insertion Sorting")
print("======================================")


# ================================
# Test Cases
# ================================
test_insertion_sort(100)
test_insertion_sort(200)
test_insertion_sort(300)