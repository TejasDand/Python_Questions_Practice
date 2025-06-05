# Find the sum of digits of a number using a while loop.

n = int(input("Enter a number: "))
sum_digits = 0

while n > 0:
    digit = n % 10          # get the last digit
    sum_digits += digit     # add it to the sum
    n = n // 10             # remove the last digit

print(f"Sum of digits: {sum_digits}")