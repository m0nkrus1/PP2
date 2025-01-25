''' Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
'''
#Arithmetic operators: +,-, *, /, %, **, //
a, b = 10, 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333...
print(a // b) # 3 (floor division)
print(a % b)  # 1 (remainder)
print(a ** b) # 1000 (10 raised to the power of 3)
#Assignment operators: =, +=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=(walrus operator)
a = 10
a += 5  # a = a + 5
print(a)  # 15
a *= 2  # a = a * 2
print(a)  # 30
#Comparison Operators:   ==, !=, >, <, >=, <=
a, b = 5, 3
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
#Logical operators: and, or, not
x = 5

print(x > 3 or x < 4)
#Identity operators: is, is not
#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)     # True (same memory location)
print(a is c)     # False (different memory locations)
print(a is not c) # True
#Bitwise operators: &, |, ^, ~, <<, >>
print(8 >> 2)
#Precedence order 
# ()
# **
# +x, -x, ~x
# * / // %
# + -
# << >>
# &
# ^
# |
# == != > >= < <= is is not in not in
# not
# and 
# or 
print(5 + 4 - 7 + 3)
