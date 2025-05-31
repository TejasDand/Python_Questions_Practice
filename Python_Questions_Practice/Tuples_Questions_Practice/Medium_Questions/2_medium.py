# Swap two variables using tuple unpacking.

tup_1 = (1, 2)

a, b = tup_1
a, b = b, a

print(a)
print(b)