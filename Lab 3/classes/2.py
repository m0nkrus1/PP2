class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


# Usage
square = Square(5)
print("Square area:", square.area())  # Output: 25

shape = Shape()
print("Default shape area:", shape.area())  # Output: 0
