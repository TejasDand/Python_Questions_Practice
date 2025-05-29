# Convert a string to title case without using  .title().

title = "times new roman book".split()

for char in title:
    print(char.capitalize(), end=" ")