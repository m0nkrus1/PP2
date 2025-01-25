#Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
#Access sets
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#NOT in a set:
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
#Add items to a set
#using add()
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#using update to add items from another set into the current set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#Remove item
#using remove()
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#using discard()
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#using pop()
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#Clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#Del will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
#Loop through the set using a for loop:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#Joining sets:
#union() - method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# We can use | operator instead of the union() method, whcih gives the same result
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
# joining multiple sets:
# joining multiple sets with the union() method:
set3 = {'apple', 'banana', 'cherry'}
my_set = set1.union(set3, set2)
print(my_set)
# using '|' (it allows to join sets with only sets)
set4 = set1 | set2 | set3
print(set4)
# Update() - inserts all items from one set into another (excludes duplicates)
# It changes the original set, and doesn't return a new set
set1.update(set2)
print(set1)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#intersection() - returns elements that in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#The '&' operator is the same as intersection()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
# intersection_update() - method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
# True, False, 1, and 0 are the same. 
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)
# difference() - method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
#The - operator is the same as difference():
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
# diiference_update() - method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
#Symmetric_difference - method will keep only the elements that are NOT present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
#The ^ operator is the same as ^:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
# Set Methods

print(set1.isdisjoint(set2))

x = {'a', 'b', 'c'}
y = {'a', 'b', 'c', 'x', 'y', 'z'}
print(x <= y) # we can use 'print(x.issubset(y))'
# '<' - sets cannot be equal, '<=' - sets can be equal

x = {'a', 'b', 'c', 'x', 'y', 'z'}
y = {'a', 'b', 'c'}
print(x >= y) # we can use 'print(x.superset(y))'
# '>' - sets cannot be equal, '>=' - sets can be equal