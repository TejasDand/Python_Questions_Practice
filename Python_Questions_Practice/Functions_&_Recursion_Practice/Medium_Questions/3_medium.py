# Write a function to find the factorial of a number using recursion.

def factorial(n):
    if n==0 or n==1: # Base Case
        return 1
    else:
        return n * factorial(n-1)  # Recursive Case

num = int(input("Enter a number: "))
result = factorial(num)

print(f"Factorial of this number '{num}' is: {result}")