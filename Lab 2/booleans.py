#Boolean Values
print(10 > 9)  # True
print(10 == 9)  # False 
print(10 < 9)  # False
print(5 > 3)   # True
print(10 == 20)  # False
print(7 != 4)    # True
'''Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.'''
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#False values
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#Functions returns Boolean values
def myFunction() :
  return True

print(myFunction())
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#Check if an object is an integer or not:

x = 200
print(isinstance(x, int))