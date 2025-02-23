import re

text = "abc abb abbb abbbb"

matches = re.findall(r'ab{2,3}', text)

if matches:
    print(matches)
else:
    print("No match found.")
