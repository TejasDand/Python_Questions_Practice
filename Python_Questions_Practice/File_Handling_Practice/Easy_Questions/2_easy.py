# How can you read the entire content of a file using Python?

with open("Text files/sample.txt", "r") as file:
    content = file.read()
    print(content)