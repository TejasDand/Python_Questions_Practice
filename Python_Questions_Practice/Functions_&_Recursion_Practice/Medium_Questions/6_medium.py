# Implement a function to calculate the power of a number using recursion.

def power(base, exponent):
    if exponent == 0:
        return 1 # base case
    else:
        return base * power(base, exponent - 1) # recursive call
    
print(power(int(input("Enter a base: ")),
            int(input("Enter a exponent: "))))