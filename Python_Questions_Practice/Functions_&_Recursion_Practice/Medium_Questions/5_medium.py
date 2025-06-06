# Write a function that accepts any number of arguments and returns their sum.

def sum_all(*args):
   return sum(args)

print(sum_all(10, 20, 30))