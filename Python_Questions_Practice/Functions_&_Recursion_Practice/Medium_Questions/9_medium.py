# Create a function to remove duplicates from a list.

def remove_duplicate_items(lst):
    unique = []
    
    for items in lst:
        if items not in unique:
            unique.append(items)
    return unique


lst = ['apple', 'banana', 'orange', 'kiwi', 'grapes', 'apple', 'orange', 'apple']
print(remove_duplicate_items(lst))