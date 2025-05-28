# Remove punctuation from a string.
import re

text = "Tejas, Aayush"

clean_text = re.sub(r'[^\w\s]', '', text)
print(clean_text)