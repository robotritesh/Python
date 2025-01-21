import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

circle1 = Circle(5)
print("Area of the circle:", circle1.calculate_area())
