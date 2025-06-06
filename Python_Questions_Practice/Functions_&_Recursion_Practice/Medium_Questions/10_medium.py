# Write a function that takes another function as input and executes it.

def add(a, b):
    print(f"A + B = {a+b}")

def executor(func, arg1, arg2):
    func(arg1, arg2)

executor(add, int(input("Enter value of A: ")),
            int(input("Enter value of B: ")))