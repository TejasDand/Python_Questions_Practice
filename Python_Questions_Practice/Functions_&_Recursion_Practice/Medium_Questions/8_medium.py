# Write a function to flatten a nested list using recursion.

def flat_list(nested_list):
    flat = []

    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flat_list(item))    # Recursive call
        else:
            flat.append(item)
    return flat
    
print(flat_list([4, 5, [9, 10, [6, 1]], 7, 8]))