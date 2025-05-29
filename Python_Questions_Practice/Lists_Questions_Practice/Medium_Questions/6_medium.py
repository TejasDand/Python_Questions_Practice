# Split a list into chunks of size  n.

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
n = 3
split_list = []

for i in range(0, len(data), n):
    split_list.append(data[i:i+n])

print(split_list)