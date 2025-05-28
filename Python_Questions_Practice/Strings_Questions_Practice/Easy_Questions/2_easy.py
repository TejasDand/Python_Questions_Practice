# Count the number of vowels in a string.

text = "Aayush"
vowel_count = 0
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        vowel_count+=1

print(f"Number of vowels in the string: {vowel_count}")