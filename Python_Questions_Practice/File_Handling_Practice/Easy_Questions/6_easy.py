# Write a program to write a list of strings to a file, each string on a new line.

fruits = ['apple', 'banana', 'grapes', 'orange', 'kiwi', 'guava', 'jackfruit', 'custard apple']

with open("Text files/fruits.txt", "w") as file:
    for word in fruits:
        upper_text = word.title()
        file.write(upper_text + "\n")