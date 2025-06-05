# Check if a number is a palindrome using loops.

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10           # Get last digit
    reverse = reverse * 10 + digit  # Build reversed number
    num = num // 10            # Remove last digit

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")