def squares(a, b):
    for i in range(a, b + 1):
        yield i **2

a = int(input("Enter the number (a): "))
b = int(input("Enter the number (b): "))

for square in squares(a, b):
    print(square)
