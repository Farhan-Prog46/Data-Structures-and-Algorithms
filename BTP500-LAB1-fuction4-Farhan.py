def recursive_function4(mystring,a, b):
 if(a >= b ):                         # 1
  return True                         # 1
 else:
  if(mystring[a] != mystring[b]):     # 1
   return False                       # 1
  else:
   return recursive_function4(mystring,a+1,b-1)
  

def function2(mystring):
 return recursive_function4(mystring, 0,len(mystring)-1)