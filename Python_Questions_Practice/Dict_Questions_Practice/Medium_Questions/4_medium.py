# Create a dictionary from two lists using  zip().

list_1 = ["Name", "Roll_No", "Salary", "State"]
list_2 = ["Tejas", 105, 15000, "Gujarat"]

merged_list = dict(zip(list_1, list_2))
print(merged_list)