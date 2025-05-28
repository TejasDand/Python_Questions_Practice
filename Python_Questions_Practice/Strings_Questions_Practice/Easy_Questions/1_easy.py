# Write a Python program to reverse a string.

string = "tejas"
reversed_text = ""

for i in range(len(string)-1, -1, -1):
    reversed_text += string[i]
    
print(reversed_text)