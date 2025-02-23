import re

def snake_to_camel(snake_str):
   
    words = snake_str.split('_')

    camel_case_str = words[0] + ''.join(word.capitalize() for word in words[1:])

    return camel_case_str

snake_case_string = "hello_world_example"
camel_case_string = snake_to_camel(snake_case_string)

print("Snake Case:", snake_case_string)
print("Camel Case:", camel_case_string)
