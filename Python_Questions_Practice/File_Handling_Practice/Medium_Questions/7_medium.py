# Write a script to reverse the content of a file line by line and save it in a new file.

with open("Text files/lines.txt", "r") as infile, open("Text files/reverse_lines.txt", "w") as outfile:
    for line in infile:
        reversed_line = line.rstrip()[::-1]
        outfile.write(reversed_line + "\n")