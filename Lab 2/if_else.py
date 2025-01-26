#If statement
a = 33
b = 200
if b > a:
  print("b is greater than a")
#Elif statement is the way of saying "if the previous conditions were not true, then try this condition".
#Else catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

# Nested If

x = 50

if x > 10:
    print("Above 10")
    if x > 20:
        print("Above 20")
    else:
        print("but not above 20")


# The pass Statement
a = 33
b = 200
if b > a:
    pass
