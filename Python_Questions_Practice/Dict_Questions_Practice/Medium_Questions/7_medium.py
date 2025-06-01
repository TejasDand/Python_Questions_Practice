# Group elements of a list into a dictionary by their first letter.
from collections import defaultdict

words = ["apple", "banana", "apricot", "cherry", "blueberry"]
grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)

print(dict(grouped))