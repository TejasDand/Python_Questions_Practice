# Create a function that takes a string and returns it reversed.

def reverse_string(text):
    reversed_text = ""

    for i in range(len(text)-1, -1, -1):
        reversed_text += text[i]

    return reversed_text

print(reverse_string(input("Enter a string: ")))