# Find the first non-repeating character.

text = "teeter"

for char in text:
    if text.count(char) == 1:
        print(char, end="")
        break
else:
    print("No, non-repeating character found!")