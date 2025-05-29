# Write a function to perform basic string compression (e.g.,  "aaabbc" →  "a3b2c1").
from collections import Counter

def string_compression(text):
    char_count = Counter(text)

    for char, count in char_count.items():
        if count > 0:
            print(f"{char}{count}",end="")

string_compression("aaabbc")