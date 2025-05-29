# Capitalize the first and last character of each word.

def capitalize_first_last(text):

    words = text.split()
    result = []

    for word in words:
        if len(word) == 1:
            result.append(word.upper())
        else:
            new_word = word[0].upper() + word[1:-1] + word[-1].upper()
            result.append(new_word)
        
    return ' '.join(result)

print(capitalize_first_last("hello world python"))