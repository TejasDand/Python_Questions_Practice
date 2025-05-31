# Sort a list of tuples based on the second element.

data = [("Alice", 25), ("Bob", 35), ("Charlie", 30)]

sorted_data = sorted(data, key=lambda x : x[1])
print(sorted_data)