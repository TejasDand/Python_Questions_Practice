# Implement a program to copy the content of one file into another file.

with open("Text files/quotes.txt", "r") as file:
    content = file.read()

with open("Text files/quotes_copy.txt", "w") as file:
    file.write(content)