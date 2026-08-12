"""
    self is not a keyword, but its a convention in python
    it refers to current instance of the class
    it must be the first parameter of the instance method, though you dont need to pass it explicitly when calling methods

    unlike some languages like java c++ , python does not have an explicit keyword
    instead self is used to access instance variables and methods inside the class 
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old.")
        #if we mention self.greet() it will call its own method, for super.greet() it will call the parent class method


p1 = Person("Alice", 30)
p1.greet()  # Output: Hello, my name is Alice and I am 30 years old.