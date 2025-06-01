# Use a dictionary to map student names to grades and calculate the average.

grades = {
    "Alice": 83,
    "Bob": 90,
    "Charlie": 75
}

total = sum(grades.values())
count = len(grades)

print(f"Average Grade: {(total/count):.1f}")