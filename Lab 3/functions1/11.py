# A function for palindrome
def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False
    
text = input('Enter string: ')
print(palindrome(text))