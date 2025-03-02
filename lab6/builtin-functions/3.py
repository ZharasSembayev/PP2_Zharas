def palindrome(text):
    text = text.lower()
    return text == text[::-1]
text = input()
if palindrome(text):
    print("The text is a palindrome.")
else:
    print("The text is not a palindrome.")