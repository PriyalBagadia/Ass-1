# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

# -> In Python, you can define a class using the class keyword followed by the class name and a colon :. 
# Inside the class definition, you can include class variables, instance variables, methods, and other attributes.

# The self keyword is used to refer to the current instance of the class. 
# It's a convention in Python to use self as the first parameter of instance methods, which allows those methods to access and 
# modify the attributes of the current object.

class Car:
    wheels = 4
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def get_make_and_model(self):
        return f"Make: {self.make}, Model: {self.model}"

car1 = Car("Toyota", "Camry")

print("Number of wheels:", car1.wheels)
print("Make and Model:", car1.get_make_and_model())
