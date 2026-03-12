def CityNames_selection_sort_descending(arr):
 n = len(arr)
 for i in range(1,n):
   temp = arr[i]
   j = i
   while j > 0 and arr[j-1] < temp:
    arr[j] = arr[j-1]
    j -= 1
    arr[j] = temp
   

    
# List of city names
cities = ['Sydney', 'Cairo', 'Mumbai', 'Paris', 'Tokyo ']
# Sort the list in descending order using selection_sort_descending function
CityNames_selection_sort_descending(cities)
# Print the sorted list
print("Sorted array in descending order:", cities)

