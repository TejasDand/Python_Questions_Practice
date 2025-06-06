# Create a function that counts vowels and consonants in a string.

def counting_vowels_consonants(text, vowel_count = 0, consonant_count = 0):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for char in text:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
        
    print(f"The text '{text}' contains {vowel_count} vowels and {consonant_count} consonants.")

counting_vowels_consonants(input("Enter a text or sentence: "))