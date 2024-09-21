# Qs. Define a Circle class to create a circle with radius r using the constructor. Define an Area() method of the class which calculates the area of the circle. Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self,redius):
        self.redius = redius

    def area(self):
        return 3.14 * self.redius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.redius

c1 = Circle((21))
print(c1.area())
print(c1.perimeter())