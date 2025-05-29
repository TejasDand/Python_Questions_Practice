# Rotate a list to the left by  k positions.

my_list = [1, 2, 3, 4, 5]
k = 3

print(my_list[k:] + my_list[:k])