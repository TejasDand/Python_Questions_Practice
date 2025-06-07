# Write a program to remove blank lines from a file and save the output to a new file.

with open("Text files/blank.txt", "r") as infile, open("Text files/no_blank.txt", "w") as outfile:
    
    for line in infile:
        if line.strip():
            outfile.write(line)