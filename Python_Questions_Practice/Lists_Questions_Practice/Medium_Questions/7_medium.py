# Find all pairs in a list that sum up to a specific value.

num_list = [1, 2, 3, 4, 5, 6]
sum_target = 6
pairs = []

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        if num_list[i] + num_list[j] == sum_target:
            pairs.append((num_list[i], num_list[j]))

print(pairs)