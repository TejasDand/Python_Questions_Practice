# Merge two sorted lists into one sorted list.

num_list1 = [4.5, 6.2, 1.2, 3.4, 6.9, 5.3, 4.2, 6.5, 9.9]
num_list2 = [6.5, 4.3, 8.9, 7.6, 4.5, 8.4, 4.7, 2.3, 8.9]

num_list1.extend(num_list2)
num_list1.sort()

print(num_list1)