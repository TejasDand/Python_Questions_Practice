# Create a recursive function to compute the nth Fibonacci number.
# Formula f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    if n <= 1: 
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
num = int(input("Enter a number: "))

for i in range(num):
    print(fibonacci(i), end=" ")