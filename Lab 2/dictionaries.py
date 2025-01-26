# Dictionary is a collection which is ordered, changeable, and does not allow duplicates.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

# Length of the dictionary
print(len(thisdict))

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

# Access items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")

# Getting all the values
print(thisdict.values())

thisdict['age'] = 40
print(thisdict.values())

thisdict['color'] = 'green'
print(thisdict.values())

if 'name' in thisdict:
    print('Yes, the name exists')

# Change values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

# Using update() - updates the dictionary with the items from the given argument
thisdict.update({"year": 2020})

# Add items
thisdict['year'] = 2024
print(thisdict)

thisdict.update({'brand': 'Ford', 'city': "Oslo"})
print(thisdict)

# Remove items
thisdict.pop('brand')  # pop() method
print(thisdict)

thisdict.popitem()  # popitem() method
print(thisdict)

del thisdict['year']
print(thisdict)  # 'del thisdict' can delete dictionary completely

# thisdict.clear()  # Clears the dictionary but doesn't delete it
# print(thisdict)

# Loop through a dictionary
for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

# Iterating through the values using the values() method
for x in thisdict.values():    
    print(x)

# Iterating through the keys using the keys() method
for x in thisdict.keys():
    print(x)

# Iterating through both keys and values using the items() method
for x, y in thisdict.items():
    print(x, y)
'''Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#Nested dictionaries

#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#Accessing Items in Nested Dictionaries
print(myfamily["child2"]["name"])

#Loop through the keys and values of all nested dictionaries:

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#Dictionary Methods
#clear()
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
my_dict.clear()
print(my_dict)  # Output: {}

#copy()
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#fromkeys() - returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)
#setdefault() - method returns the value of the item with the specified key. If the key does not exist, inserts the key with a specified value.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

