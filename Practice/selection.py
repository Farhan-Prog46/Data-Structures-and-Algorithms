def CityNames_selection_sort_descending(arr):
 n = len(arr)
 for i in range(n-1):
  min_idx = i
  for j in range(i+1, n):
   if arr[j] > arr[min_idx]:
    min_idx = j

    if min_idx != i:
     arr[i], arr[min_idx] = arr[min_idx], arr[i]
   

    
# List of city names
cities = ['Sydney', 'Cairo', 'Mumbai', 'Paris', 'Tokyo ']
# Sort the list in descending order using selection_sort_descending function
CityNames_selection_sort_descending(cities)
# Print the sorted list
print("Sorted array in descending order:", cities)

