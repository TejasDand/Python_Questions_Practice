# Invert a dictionary (swap keys and values).

dict1 = {"Name" : "Tejas", "Age" : 19, "Salary" : 150}

inverted = {value : key for key, value in dict1.items()}
print(inverted)