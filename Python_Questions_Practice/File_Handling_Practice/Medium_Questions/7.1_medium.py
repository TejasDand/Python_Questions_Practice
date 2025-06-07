# Reversing the order of lines.

with open("Text files/lines.txt", "r") as infile:
    lines = infile.readlines()
    reversed_order_line = lines[::-1]

with open("Text files/reverse_order_line.txt", "w") as outfile:
    for line in reversed_order_line:
        outfile.write(line)