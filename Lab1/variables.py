#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
# Assign multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# One value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
#Unpack a List
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#Output variables
x = "Python is awesome"
print(x)
x = 5
y = 10
print(x + y)
#Global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)