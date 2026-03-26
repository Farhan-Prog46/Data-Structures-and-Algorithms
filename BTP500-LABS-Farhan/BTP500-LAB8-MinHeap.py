# ==========================================================
# Course Code : BTP500
# Lab         : Lab 08
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID  : 154614232
# Topic       : MinHeap
# ==========================================================
import heapq

countries = ["Peru","Bolivia","Brazil","Chile","Colombia","Ecuador",
             "Guyana","Paraguay","Argentina","Suriname","Uruguay","Venezuela"]

credits = [2500,3500,1000,5000,1000,500,200,15000]

min_heap = []

for num in credits:
    heapq.heappush(min_heap, num)

print("Min Heap (Credits):")
print(min_heap)

# HEAP SORT
sorted_list = []
while min_heap:
    sorted_list.append(heapq.heappop(min_heap))

print("\nSorted (Ascending):", sorted_list)

print("\nHeight:", len(sorted_list))