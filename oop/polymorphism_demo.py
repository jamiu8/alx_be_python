import math

class Shape:
    def area(self):
        # This ensures derived classes must override the method
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Override to calculate rectangle area
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Override to calculate circle area
        return math.pi * (self.radius ** 2)
