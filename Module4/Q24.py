# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius ** 2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

circle1 = Circle(5)

area = circle1.compute_area()
perimeter = circle1.compute_perimeter()

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)
