# Filter a dictionary to keep only keys with values above a threshold.

scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 60}
threshold = 80

filtered = {key : value for key, value in scores.items() if value > threshold}
print(filtered)