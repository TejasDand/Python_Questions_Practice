# Write a function to check if a string is a palindrome.

def checking_string_palindrome(text):
    reverse_text = ""

    for i in range(len(text)-1, -1, -1):
        reverse_text += text[i]

    if text == reverse_text:
        print("Yes, string is palindrome.")
    else:
        print("No, string is not palindrome.")

checking_string_palindrome(input("Enter a string: "))