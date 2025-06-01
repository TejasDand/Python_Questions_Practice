# Count the frequency of characters in a string using a dictionary.

text = "madam"
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)