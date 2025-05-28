# Count occurrences of a specific character.

text = input("Enter a string: ")
character = input("Enter a character to count: ")

count = text.lower().count(character)
print(f"The character '{character}' appears {count} times in the string.")