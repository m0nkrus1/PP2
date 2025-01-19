#Strings
print("Hello")
print('Hello')
#Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
#Assign String to a Variable
a = "Hello"
print(a)
#Multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Looping Through a String
for x in "banana":
  print(x)
#String Length
a = "Hello, World!"
print(len(a))
#Check string
txt = "The best things in life are free!"
print("free" in txt)
#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

#Slicing strings
b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])
b = "Hello, World!"
print(b[2:])
b = "Hello, World!"
print(b[-5:-2])
#Modify strings: upper case, lower case, remove whitespace
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.lower())
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#Concatenate strings
a = "Hello"
b = "World"
c = a + b
print(c)
#F-strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#Performing a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)
#Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
txt = "Hello\nWorld!"
print(txt) 
#String Methods
text1 = "hello world"
text2 = "PYTHON"
text3 = "12345"
text4 = "Hello123"
text5 = "   spaced text   "
text6 = "apple,banana,orange"
text7 = "HELLO WORLD"
text8 = "Title Case Text"
text9 = "hello\tworld"
text10 = "line1\nline2\nline3"
text11 = "Python is fun"
text12 = "   "
text13 = "ß"
text14 = "hello123"
text15 = "data.csv"
text16 = "python"

# 1. capitalize()
print(text1.capitalize())  # Hello world

# 2. casefold()
print(text13.casefold())  # ss (handles special characters)

# 3. center()
print(text1.center(20, "-"))  # ----hello world-----

# 4. count()
print(text1.count("o"))  # 2

# 5. encode()
print(text1.encode())  # b'hello world'

# 6. endswith()
print(text15.endswith(".csv"))  # True

# 7. expandtabs()
print(text9.expandtabs(4))  # hello   world

# 8. find()
print(text1.find("world"))  # 6

# 9. format()
print("My name is {} and I love {}.".format("Alice", "Python"))  # My name is Alice and I love Python.

# 10. format_map()
data = {"name": "Bob", "language": "Java"}
print("My name is {name} and I love {language}.".format_map(data))  # My name is Bob and I love Java.

# 11. index()
print(text1.index("world"))  # 6

# 12. isalnum()
print(text4.isalnum())  # True

# 13. isalpha()
print(text1.isalpha())  # False

# 14. isascii()
print(text1.isascii())  # True

# 15. isdecimal()
print(text3.isdecimal())  # True

# 16. isdigit()
print(text3.isdigit())  # True

# 17. isidentifier()
print("python3".isidentifier())  # True

# 18. islower()
print(text1.islower())  # True

# 19. isnumeric()
print("Ⅻ".isnumeric())  # True

# 20. isprintable()
print(text1.isprintable())  # True

# 21. isspace()
print(text12.isspace())  # True

# 22. istitle()
print(text8.istitle())  # True

# 23. isupper()
print(text7.isupper())  # True

# 24. join()
print("-".join(["Python", "is", "fun"]))  # Python-is-fun

# 25. ljust()
print(text1.ljust(20, "*"))  # hello world*********

# 26. lower()
print(text2.lower())  # python

# 27. lstrip()
print(text5.lstrip())  # "spaced text   "

# 28. maketrans() and translate()
trans = str.maketrans("ae", "12")
print("apple".translate(trans))  # 1ppl2

# 29. partition()
print(text1.partition(" "))  # ('hello', ' ', 'world')

# 30. replace()
print(text1.replace("world", "Python"))  # hello Python

# 31. rfind()
print(text1.rfind("o"))  # 7

# 32. rindex()
print(text1.rindex("o"))  # 7

# 33. rjust()
print(text1.rjust(20, "*"))  # *********hello world

# 34. rpartition()
print(text1.rpartition(" "))  # ('hello', ' ', 'world')

# 35. rsplit()
print(text6.rsplit(",", 1))  # ['apple,banana', 'orange']

# 36. rstrip()
print(text5.rstrip())  # "   spaced text"

# 37. split()
print(text6.split(","))  # ['apple', 'banana', 'orange']

# 38. splitlines()
print(text10.splitlines())  # ['line1', 'line2', 'line3']

# 39. startswith()
print(text1.startswith("hello"))  # True

# 40. strip()
print(text5.strip())  # "spaced text"

# 41. swapcase()
print(text7.swapcase())  # hello world

# 42. title()
print(text1.title())  # Hello World

# 43. upper()
print(text1.upper())  # HELLO WORLD

# 44. zfill()
print(text3.zfill(8))  # 00012345