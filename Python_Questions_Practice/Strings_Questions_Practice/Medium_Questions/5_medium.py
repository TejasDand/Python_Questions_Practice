# Remove all characters except alphabets from a string.
import re

text = "Room 105!||"
matches = re.sub(r'[^a-zA-Z]', '', text)    # This match any character that is NOT a letter

print(matches)