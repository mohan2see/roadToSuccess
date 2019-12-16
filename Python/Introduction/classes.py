"""
Objects are instances of a class. Class are real world things and situations. creating objects of a class is called
instantiation. each object can have its own behaviour.
"""


class Fruits:
    """ A simple Fruits class"""

    def __init__(self, name, color):
        """ default method invoked by python whenever an object is instantiated. The variables prefixed with self
        is available to all the methods in the class. A method is nothing but a function in a class. The __ in init
        method is a conventions to prevent pythons default method conflicting with your own method """
        self.name = name
        self.color = color

    def shape(self, shape):
        """ Shape of the fruit"""
        print(f"{self.name} is in {shape} shape")

    def taste(self, taste):
        """ Taste of the fruit"""
        print(f"{self.name} tastes {taste}")


# making an instance of a class
my_fruit = Fruits('Apple', 'red')
# my_fruit is the object that can access all the methods of Fruits class
print(f"my fruit name is {my_fruit.name}")
my_fruit.shape('Oval')
my_fruit.taste("Sweet")

# creating multiple instances(objects) with its own property
another_fruit = Fruits('Orange', 'orange')
print(f"my fruit name is {another_fruit.name}")
another_fruit.shape('round')
another_fruit.taste("Kind of sweet")


""" modifying the attributes associated with the instance"""
""" To make the class more interesting, let’s add an attribute that changes
over time. We’ll add an attribute that stores the car’s overall mileage."""


# adding a method for odometer reading

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def odometer_read(self):
        print(f"This car has {self.odometer_reading} miles on it")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
# printing the default odometer value which is '0'
my_new_car.odometer_read()
# modifying the instance attribute
my_new_car.odometer_reading = 5000
# printing the modified odometer value which is '5000'
my_new_car.odometer_read()

#newly added line


