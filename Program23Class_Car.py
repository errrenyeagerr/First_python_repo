"""
    This is the first program of classes in python including car as a class and its attributes and methods.
"""

class Car:

    # Constructor Method
    def __init__(self, brand, color, wheels):
        self.brand = brand      # Instance Attribute
        self.color = color      # Instance Attribute
        self.wheels = wheels    # Instance Attribute

    # Method
    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")

# Create instances of Car
car1 = Car("Toyota", "Red", "Neo Wheel")
car2 = Car("Honda", "Blue", "15' Alloy Wheel")

# Accessing attributes and methods
print(car1.brand)
print(car2.color)
print(car2.wheels)
car1.drive()
car2.drive()
