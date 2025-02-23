import re

text = "Hello world Test Case Example_Test anotherExample"
pattern = r'\b[A-Z][a-z]+\b'  

matches = re.findall(pattern, text)

if matches:
    print("Matching sequences:", matches)
else:
    print("No match found.")
