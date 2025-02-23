import re

text = "Hello, world. This is a test, let's replace spaces, commas, and dots."

x = r'[ ,.]'

modified_text = re.sub(x, ":", text)

print("Original text:", text)
print("Modified text:", modified_text)
