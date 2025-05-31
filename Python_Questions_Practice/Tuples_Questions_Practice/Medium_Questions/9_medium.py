# Merge two tuples element-wise into a list of tuples.

tup1 = (1, 2, 3)
tup2 = ('a', 'b', 'c')

merged_list = list(zip(tup1, tup2))
print(merged_list)