import re

def split_at_uppercase(text):
   
    words = re.findall(r'[A-Z][a-z]*', text)
    return words

my_text = "HelloWorldExample"
result = split_at_uppercase(my_text)

print("Original String:", my_text)
print("Split Words:", result)
