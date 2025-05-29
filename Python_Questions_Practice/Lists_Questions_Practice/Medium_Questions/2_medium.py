# Flatten a 2D list into a 1D list.

matrix = [[1, 2], [3, 4], [5, 6]]
flat_list = []

for sub_list in matrix:
    for item in sub_list:
        flat_list.append(item)

print(flat_list)