# Count the frequency of each element in a list and return as a dictionary.
from collections import Counter

my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq = Counter(my_list)

print(dict(freq))