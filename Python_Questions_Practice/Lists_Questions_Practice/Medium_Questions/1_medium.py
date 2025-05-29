# Remove duplicates from a list without using  set().

fruits_list = ['apple', 'banana', 'orange', 'kiwi', 'grapes', 'apple', 'orange', 'apple']
unique = []

for item in fruits_list:
    if item not in unique:
        unique.append(item)

print(unique)