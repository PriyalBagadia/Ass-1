# Write a Python program to calculate surface volume and area of a cylinder

import math

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

# Test the functions
radius = 3
height = 5
surface_area = cylinder_surface_area(radius, height)
volume = cylinder_volume(radius, height)

print("Surface Area of the cylinder:", surface_area)
print("Volume of the cylinder:", volume)
