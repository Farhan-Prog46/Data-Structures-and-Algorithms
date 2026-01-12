def function3(list):
 n = len(list)
 for i in range(n - 1):
  for j in range(n - 1 - i):
   if list[j] > list[j+1]:
      tmp = list[j]
      list[j] = list[j+1]
      list[j + 1] = tmp
      