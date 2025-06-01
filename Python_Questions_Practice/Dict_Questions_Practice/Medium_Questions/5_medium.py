#  Sort a dictionary by its keys or values.

my_dict = {'a':1, 'b':3, 'd':4, 'f':7, 'c':2, 'e':6}

# Sort by keys
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)

# Sort by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)