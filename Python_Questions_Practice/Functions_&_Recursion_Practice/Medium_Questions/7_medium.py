# Write a function to return all prime numbers in a range.

def prime_numbers(range_n):
    
    for num in range(2, range_n):
        is_Prime = True
    
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_Prime = False
                break

        if is_Prime:
            print(num, end=" ")

prime_numbers(int(input("Enter a range: ")))