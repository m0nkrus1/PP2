import re

text = "hello_world test_case Example_Test another_example"

x = r'\b[a-z]+_[a-z]+\b'
matches = re.findall(x, text)
if matches:
    print("Matching sequences:", matches)
else:
    print("No match found.")
