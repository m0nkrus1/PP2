import re

my_text = 'HereIsSomeData'

formatted_text = re.sub(r'(?<=[a-z])([A-Z])', r' \1', my_text)

print(formatted_text)
