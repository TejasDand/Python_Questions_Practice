# Remove duplicate values from a dictionary.

my_dict = {'a':1, 'b':3, 'd':4, 'f':7, 'c':2, 'e':6, 'c':1, 'b':3}
unique_values = set()
new_dict = {}

for key, value in my_dict.items():
    if value not in unique_values:
        new_dict[key] = value
        unique_values.add(value)

print(new_dict)