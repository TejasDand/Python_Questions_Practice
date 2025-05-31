# Write a function that returns multiple values using a tuple.

def calculate(a, b):
    return (a + b, a - b, a * b, a / b)

result = calculate(4, 5)
print(result)
print(type(result))