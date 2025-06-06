# Write a function that returns the maximum of three numbers.

def largest_number(num1, num2, num3):
    
    if (num1 > num2) and (num1 > num3):
        print(f"{num1} is largest number.")
    
    elif (num2 > num1) and (num2 > num3):
        print(f"{num2} is largest number.")
    
    else:
        print(f"{num3} is largest number.")

largest_number(int(input("Enter first number: ")),
               int(input("Enter second number: ")),
               int(input("Enter third number: ")))