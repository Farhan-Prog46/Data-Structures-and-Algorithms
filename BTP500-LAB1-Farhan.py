def fibonacci(n):
    """
    Function Name: fibonacci
    Purpose: Generate the first n Fibonacci numbers
    Big-O Time: n
    Big-O Space: n
    
    """
    FibonacciSeries = []         # 1

    a = 0                        # 1
    b = 1                        # 1

    for i in range(n):           # n + 1
                                 # n times to "advance i" through the loop 
                                 # +1 for the loop/range setup (constant)

        FibonacciSeries.append(a) # 1 * n (constant work each iteration)
        a, b = b, a + b           # 2 * n 
                                  # 1 for the + operation (a + b)
                                  # 1 for the assignment/update (updating a and b)
                                  # happens n times
                                  
    return FibonacciSeries         # 1 


print("Name: Syed Farhan Zaheer Hussainy")
print("Lab Number: 1")
print("Algorithm Name: Fibonacci Series")
print("------------------------------------")

print(f"n = 5  -> {fibonacci(5)}")
print(f"n = 17 -> {fibonacci(17)}")
print(f"n = 37 -> {fibonacci(37)}")