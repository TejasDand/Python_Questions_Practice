# Write a Python script that reads a text file and prints only the lines that contain the word  "error".

with open("Text files/error.txt", 'r') as file:
    for line in file:
        if 'error' in line.lower():
            print(line.strip())