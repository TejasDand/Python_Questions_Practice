# Write a Python program to read a file and count the number of lines in it.

with open("Text files/quotes.txt") as file:
    count = sum(1 for _ in file)
    
print(f"There are {count} lines in the quotes.txt file.")