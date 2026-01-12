def fibonacci(n):
    """
    Function Name: fibonacci
    Purpose: Generate the first n Fibonacci numbers
    Big-O Time: n
    Big-O Space: n
    
    """
    FibonacciSeries = []

    a = 0
    b = 1

    for i in range(n):
        FibonacciSeries.append(a)
        a, b = b, a + b

    return FibonacciSeries


print("Name: Syed Farhan Zaheer Hussainy")
print("Lab Number: 1")
print("Algorithm Name: Fibonacci Series")
print("------------------------------------")

print(f"n = 5  -> {fibonacci(5)}")
print(f"n = 17 -> {fibonacci(17)}")
print(f"n = 37 -> {fibonacci(37)}")