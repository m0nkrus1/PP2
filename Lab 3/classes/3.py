class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 3)
print("Rectangle area:", rectangle.area())  # Output: 15
shape = Shape()
print("Default shape area:", shape.area())  # Output: 0
