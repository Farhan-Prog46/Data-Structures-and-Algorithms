def function2(number):
 return (number * (number + 1) * (2 * number + 1)) // 6

"""
(number + 1)              - 1
(2 * number)              - 1
(2 * number + 1)          - 1
number * (number + 1)     - 1
result * (2 * number + 1) - 1
integer division // 6     - 1
return - 1

Total operations = 7
"""