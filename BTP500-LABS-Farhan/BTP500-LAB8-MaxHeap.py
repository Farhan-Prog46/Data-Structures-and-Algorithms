# ==========================================================
# Course Code : BTP500
# Lab         : Lab 08
# Student Name: Syed Farhan Zaheer Hussainy
# Student ID  : 154614232
# Topic       : MaxHeap
# ==========================================================
import heapq

countries = ["Peru","Bolivia","Brazil","Chile","Colombia","Ecuador",
             "Guyana","Paraguay","Argentina","Suriname","Uruguay","Venezuela"]

credits = [2500,3500,1000,5000,1000,500,200,15000]

# MAX HEAP (use negative values)
max_heap = []

for num in credits:
    heapq.heappush(max_heap, -num)

print("Max Heap (Credits):")
for val in max_heap:
    print(-val)

# HEAP SORT
sorted_list = []
while max_heap:
    sorted_list.append(-heapq.heappop(max_heap))

print("\nSorted (Descending):", sorted_list)

print("\nHeight:", len(sorted_list))