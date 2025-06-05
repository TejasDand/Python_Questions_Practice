# Use a loop to find the GCD of two numbers.

a = 36
b = 60

gcd = 1

# Loop from 1 to the smallest of a or b
for i in range(1, min(a, b) + 1): 
    if a % i == 0 and b % i == 0:
        print(i)
        gcd = i # update gcd whenever we find a common divisor

print(f"GCD is: {gcd}")