def function5(value, number):
 if (number == 0):    # constant
  return 1
 elif (number == 1):  # constant
  return value
 else:
  half = number // 2  # constant
 result = function5(value, half)
 if (number % 2 == 0):    # constant
  return result * result  # constant
 else:
  return value * result * result   # constant
 
 # one recursive call with number / 2