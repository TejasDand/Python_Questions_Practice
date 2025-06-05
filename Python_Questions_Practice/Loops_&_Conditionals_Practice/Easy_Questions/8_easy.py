# Count the number of vowels in a string using a loop.

text = "Apple Banana bhai bhai!"
vowels = ["a", "e", "i", "o", "u"]
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Total number of vowels in a string is: {count}")