# Find the largest of three numbers using  if-elif-else.

print("---- Finding the largest number among 3 numbers ----")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


if (num1 > num2) and (num1 > num3):
    print(f"\nFirst number is largest among 3 numbers: {num1}")
elif (num2 > num1) and (num2 > num3):
    print(f"\nSecond number is largest among 3 numbers: {num2}")
else:
    print(f"\nThird number is largest among 3 numbers: {num3}")