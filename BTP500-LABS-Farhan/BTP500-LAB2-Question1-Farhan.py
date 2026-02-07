# ----------------------------------------
# Course: BTP500
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID: 154714232
# Lab: 02 - Question 1 (Search Algorithms)
# ----------------------------------------

import random
import time


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search_iterative(arr, key):
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


def binary_search_recursive(arr, key, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        return binary_search_recursive(arr, key, mid + 1, right)
    else:
        return binary_search_recursive(arr, key, left, mid - 1)


def run_one_case(arr, sorted_arr, target, case_name):
    print(f"{case_name} Search")
    print(f"Item searched: {target}")

    start = time.time()
    idx_linear = linear_search(arr, target)
    t_linear = time.time() - start

    start = time.time()
    idx_bin_iter = binary_search_iterative(sorted_arr, target)
    t_bin_iter = time.time() - start

    start = time.time()
    idx_bin_rec = binary_search_recursive(sorted_arr, target, 0, len(sorted_arr) - 1)
    t_bin_rec = time.time() - start

    print(f"Linear Search Index      : {idx_linear}")
    print(f"Iterative Binary Index   : {idx_bin_iter}")
    print(f"Recursive Binary Index   : {idx_bin_rec}")

    print(f"Linear Search Time       : {t_linear:.6f} seconds")
    print(f"Iterative Binary Time    : {t_bin_iter:.6f} seconds")
    print(f"Recursive Binary Time    : {t_bin_rec:.6f} seconds")

    times = {
        "Linear Search": t_linear,
        "Iterative Binary Search": t_bin_iter,
        "Recursive Binary Search": t_bin_rec
    }
    best = min(times, key=times.get)
    print("Best Performing Algorithm:", best)
    print("--------------------------------------")


def test_searches(n):
    print(f"\nTesting for n = {n}")

    arr = [random.randint(1, 1000) for _ in range(n)]
    sorted_arr = sorted(arr)

    successful_target = random.choice(arr)
    run_one_case(arr, sorted_arr, successful_target, "Successful")

    unsuccessful_target = -1
    run_one_case(arr, sorted_arr, unsuccessful_target, "Unsuccessful")


print("======================================")
print("Course Code: BTP500")
print("Student Name: Syed Farhan Zaheer Hussainy")
print("Student ID: 154714232")
print("Lab 02 - Question 1 (Search Algorithms)")
print("======================================")

for size in [10, 20, 30]:
    test_searches(size)
