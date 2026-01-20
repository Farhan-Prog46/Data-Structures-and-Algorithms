# ----------------------------------------
# Course: BTP500
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID: 154714232
# Lab: 02 - Question 2 (Sorting Algorithms)
# ----------------------------------------

import random
import time


def insertion_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j > 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
    return arr

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0 , n -i- 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        key = i
        for j in range (i + 1, n):
            if arr[j] < arr[key] :
                key = j
            arr[i], arr[key] = arr[key], arr[i]
    return arr


def test_sorts(n):
    print(f"Testing for n = {n}")

    arr = [random.randint(1, 1000) for _ in range(n)]

    start = time.time()
    insertion_sort(arr)
    t_insertion = time.time() - start

    start = time.time()
    bubble_sort(arr)
    t_bubble = time.time() - start

    start = time.time()
    selection_sort(arr)
    t_selection = time.time() - start

    print(f"Insertion Sort Time : {t_insertion:.6f} seconds")
    print(f"Bubble Sort Time    : {t_bubble:.6f} seconds")
    print(f"Selection Sort Time : {t_selection:.6f} seconds")

    times = {
        "Insertion Sort": t_insertion,
        "Bubble Sort": t_bubble,
        "Selection Sort": t_selection
    }

    best = min(times, key=times.get)
    print("Best Performing Algorithm:", best)
    print("--------------------------------------\n")


print("======================================")
print("Course Code: BTP500")
print("Student Name: Syed Farhan Zaheer Hussainy")
print("Student ID: 154714232")
print("Lab 02 - Question 2 (Sorting Algorithms)")
print("======================================\n")

for size in [100, 200, 300]:
    test_sorts(size)