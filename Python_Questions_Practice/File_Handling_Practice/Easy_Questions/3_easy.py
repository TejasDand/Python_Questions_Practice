# Write a program to append the line  "New Line" to an existing file  sample.txt.

with open("Text files/sample.txt", "a") as file:
    file.write("New Line!")