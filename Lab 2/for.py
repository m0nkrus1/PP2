#For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#continue statement stops the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#range()  returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number(exclusive).
#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# The 'pass' Statement
# 'for loops' cannot be empty, so it you want to leave 'for loop' with no content, 
# put in the 'pass' statement to avoid getting an error

for x in [0, 1, 2]:
    pass
