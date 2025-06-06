# Write a function to check if a number is even or odd.

def even_or_odd(num):
    if num % 2 == 0:
        print(f"Even: {num}")
    else:
        print(f"Odd: {num}")

even_or_odd(int(input("Enter a number: ")))