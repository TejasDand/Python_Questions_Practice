# Check if one string is a rotation of another.

def is_rotation(str1, str2):

    if len(str1) != len(str2):
        return False
    return str2 in (str1 + str1)

print(is_rotation("hello", "lohel"))
print(is_rotation("hello", "elloh"))
print(is_rotation("hello", "hlelo")) 