def function3(list):
 n = len(list)                # 1
 for i in range(n - 1):       # (n - 1) + 1 
  for j in range(n - 1 - i):  # (n - 1 - i) + 1
   if list[j] > list[j+1]:    # (n - 1 - i) comparisons
      tmp = list[j]           # (n - 1 - i) 
      list[j] = list[j+1]     # (n - 1 - i) 
      list[j + 1] = tmp       # (n - 1 - i) 
      