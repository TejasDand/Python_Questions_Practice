# Reverse a number using loops.

n = 123
reverse = 0

while n > 0:
    digit = n % 10                      # Get last digit - 3, 2, 1
    reverse = reverse * 10 + digit      # Build reversed number - 3, 32, 321
    n = n // 10                         # Remove last digit - 12, 1, 0

print(f"Reverse number is: {reverse}")