# Create a list of squares of even numbers from another list.

numbers = [1, 2, 3, 4, 5, 6]
square_list = []

for items in numbers:
    if items % 2 == 0:
        square_list.append(items ** 2)

print(square_list)