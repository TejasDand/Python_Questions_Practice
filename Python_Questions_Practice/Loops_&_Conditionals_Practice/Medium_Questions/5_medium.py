# Count digits, letters, and special characters in a string.

text = input("Enter a string: ")

letters = 0
digits = 0
special_chars = 0

for char in text:
    if char.isalpha():
        letters += 1
        
    elif char.isdigit():
        digits += 1
        
    else:
        special_chars += 1

print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Special Characters: {special_chars}")