# Create a nested dictionary and access inner values.

students = {
    "Tejas" : {"Math":90, "English":85},
    "Amit" : {"Math":78, "English":88}
}

# Accessing a value from the nested dict
print(students["Amit"]["English"])

# Updating a value from the nested dict
students["Tejas"]["Math"] = 95
print(students)