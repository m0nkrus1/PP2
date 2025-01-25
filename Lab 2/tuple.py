#Tuples
mytuple = ("apple", "banana", "cherry")
#Tuple length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#Tuple any data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
#Access tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Update Tuples
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# We can convert a tuple into a list, change it and convert the list back into a tuple
x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'mango'
y.append("orange")
x = tuple(y)
print(x)
# It is allowed  to add tuples to tuples

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#Unpack Tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#Using Asterisk
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#Loop through 
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Using a While Loop

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#Join tuples 
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
#Tuple methods
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)
