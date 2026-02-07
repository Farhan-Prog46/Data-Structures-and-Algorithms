# ----------------------------------------
# Course: BTP500
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID: 154714232
# Lab: 02
# ----------------------------------------

import time
import random

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range (0, n - i- 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def test_bubble_sort(n):
    print(f"Testing Bubble Sort for n = {n}")

    arr = [random.randint(1, 1000) for _ in range(n)]

    start = time.time()
    bubble_sort(arr)
    elapsed_time = time.time() - start

    print(f"Bubble Sort Time: {elapsed_time:.6f} seconds")
    print("--------------------------------------\n")

print("======================================")
print("Course Code: BTP500")
print("Student Name: Syed Farhan Zaheer Hussainy")
print("Student ID: 154714232")
print("Lab 02 - Bubble Sorting")
print("======================================")

# ================================
# Test Cases
# ================================
test_bubble_sort(100)
test_bubble_sort(200)
test_bubble_sort(300)