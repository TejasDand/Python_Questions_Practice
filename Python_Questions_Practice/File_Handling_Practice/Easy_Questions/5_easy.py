# Write a program to open a file in read mode and print the first 5 characters.

with open("Text files/sample.txt", "r") as file:
    content = file.read(5)  # reads only first 5 characters
    print(content)