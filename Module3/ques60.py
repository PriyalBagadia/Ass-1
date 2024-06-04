# Write a Python program to calculate the area of a trapezoid

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

# Test the function
base1 = 5
base2 = 9
height = 4
area = trapezoid_area(base1, base2, height)
print("The area of the trapezoid is:", area)
