#  Read a file  scores.txt and display only the top 3 lines with the highest numbers.

with open("Text files/scores.txt", "r") as file:
    lines = file.readlines()

# Convert each line to an integer and remove newline characters
numbers = [int(line.strip()) for line in lines]

# Sort the numbers in descending order
numbers.sort(reverse=True)

# Print top 3
for score in numbers[:3]:
    print(score)