# Find all duplicate characters in a string.
from collections import Counter

text = "banana"
char_count = Counter(text)

for char, count in char_count.items():
    if count > 1:
        print(f"'{char}' appears {count} times")