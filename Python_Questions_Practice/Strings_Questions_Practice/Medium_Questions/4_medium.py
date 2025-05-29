#  Implement a custom  split() method.

def custom_split(string, delimiter):
    result = []
    word = ""

    for char in string:
        if char == delimiter:
            result.append(word)
            word = ""
        else:
            word += char
    result.append(word) # Add last word
    return result


print(custom_split("manipal university jaipur", " "))