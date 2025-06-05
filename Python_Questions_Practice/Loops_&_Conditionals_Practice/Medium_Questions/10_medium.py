# Check if a number is an Armstrong number.
'''
Example: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
Since the sum is equal to the number itself → 153 is an Armstrong number
'''

num = 153
temp = num
n_digits = len(str(num)) # 3
sum_of_powers = 0

while temp > 0:
    digit = temp % 10                     # Get last digit - 3, 5, 1
    sum_of_powers += digit ** n_digits    # 27 + 125 = 152 | 152 + 1 = 153
    temp //= 10                           # Remove last digit - 15, 1, 0

if sum_of_powers == num:
    print(f"{num} is an Armstrong Number!")
else:
    print(f"{num} is not an Armstrong Number!")