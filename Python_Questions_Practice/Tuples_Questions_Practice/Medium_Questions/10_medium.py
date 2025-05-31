# Remove duplicate tuples from a list of tuples.

data = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4)]
unique_data = []
seen  = set()

for item in data:
    if item not in seen:
        unique_data.append(item)
        seen.add(item)

print(unique_data)