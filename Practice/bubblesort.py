def CityNames_selection_sort_descending(arr):
 n = len(arr)
 for i in range(n-1):
  for j in range(n-1-i):
   if arr[j] < arr[j+1]:
    arr[j+1], arr[j] = arr[j], arr[j+1]
   

    
# List of city names
cities = ['Sydney', 'Cairo', 'Mumbai', 'Paris', 'Tokyo ']
# Sort the list in descending order using selection_sort_descending function
CityNames_selection_sort_descending(cities)
# Print the sorted list
print("Sorted array in descending order:", cities)

