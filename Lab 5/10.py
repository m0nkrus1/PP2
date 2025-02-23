import re

def camel_to_snake(text):
    snake_case = re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower()
    return snake_case

my_text = "CamelCaseToSnakeCase"
result = camel_to_snake(my_text)

print("Original String:", my_text)
print("Snake Case:", result)
