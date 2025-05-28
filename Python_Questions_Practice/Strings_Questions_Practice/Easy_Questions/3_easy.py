# Check if a string is a palindrome.

text = "madam"
reversed_text = ""

for i in range(len(text)-1, -1, -1):
   reversed_text += text[i]

if reversed_text == text:
   print("Yes, it is a palindrome!")
else:
   print("No, it is not a palindrome!")