class Car:
    """A simple Car class"""

    def __init__(self, make, model, year):  # Constructor (special method)
        self.make = make
        self.model = model
        self.year = year

    def accelerate(self):
        print(f"The {self.make} {self.model} is accelerating!")

    def brake(self):
        print(f"The {self.make} {self.model} is braking!")

# Create objects (instances) of the Car class
my_car = Car("Ford", "Mustang", 2023)
another_car = Car("Toyota", "Camry", 2022)

# Access object attributes
print(f"Make: {my_car.make}")  # Output: Make: Ford
print(f"Model: {my_car.model}")  # Output: Model: Mustang
print(f"Year: {my_car.year}")  # Output: Year: 2023

# Call object methods
my_car.accelerate()  # Output: The Ford Mustang is accelerating!
another_car.brake()  # Output: The Toyota Camry is braking!


print(__name__)

import mymodule

print(mymodule.add(1,2))
print(__name__)