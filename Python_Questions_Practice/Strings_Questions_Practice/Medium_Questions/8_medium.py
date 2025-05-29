# Count the number of words in a sentence.
import re

sentence = "Hello, how are you today?"
sentence = re.sub(r'[^\w\s]', '', sentence)

words = sentence.split()
# print(words)

print(len(words))