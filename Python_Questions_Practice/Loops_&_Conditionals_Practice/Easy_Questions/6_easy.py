# Print the multiplication table of a given number.

table_num = int(input("Enter a number: "))

for i in range(1, 10+1):
    print(f"{table_num} x {i} = {table_num*i}")