def bubble_sort_strings(arr, order="asc"):
   n = len(arr)
   for i in range(1, n):
      temp = arr[i]
      j = i

      while j > 0 and order == "asc" and arr[j - 1] > temp : 
         arr [j] = arr[j-1]
         j -= 1
         arr[j] = temp
   return arr
# Sample list of strings
names = ["Zara", "Alice", "John", "Bob", "Emma"]

# Ascending sort
ascending = bubble_sort_strings(names.copy(), "asc")
print("Ascending Order:", ascending)

# Descending sort
descending = bubble_sort_strings(names.copy(), "desc")
print("Descending Order:", descending)