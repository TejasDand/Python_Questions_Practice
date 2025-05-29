# Implement a custom function that mimics the  index() method.

def custom_index(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    
    raise ValueError(f"{value} not found in the list.")

print(custom_index([10, 20, 30, 40, 50], 30))