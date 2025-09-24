# Abstraction 
# Hiding the implementation details of a class and only showing the essential features to the user.
#  1)Abstract Base Class ---> its  from abc import ABC 
#  2)AbstractMethod ----> a method which is compusory to used in child class  

import math
from abc import ABC, abstractmethod

class Shape(ABC):  # Inherit from ABC to make it an abstract class
    @abstractmethod
    def printarea(self):  # Correct method signature
        pass

class Rectangle(Shape):
    type = "Rectangle"
    side = 4

    def __init__(self):
        self.length =  int(input("Enter the Length of the Rectangle... "))
        self.width = int(input("Enter the Width of the Rectangle.... "))
        

    def printarea(self):  # Implement the abstract method
        return f"The Area of rectangle is {self.length * self.width}"
    
class circle(Shape):
    def __init__(self):
        self.radius = int(input("Enter the Radius of the Circle... "))

    def printarea(self): # if I write a Abstract method .it is coumpusory to write in Every child class
        return f"The Area of Circle is {int(math.pi*self.radius**2)}"
        
class Squre(Shape):
    def __init__(self):
        self.length = int(input("Enter the Length of the Squre... "))
        self.width = int(input("Enter the Width of the Squre... "))

    def printarea(self):  # Implement the abstract method
        return f"The Area of rectangle is {self.length * self.width}"
        


# Test
r1 = Rectangle()
print(r1.printarea())  # Output: 42

c1=circle()
print(c1.printarea())

s1=Squre()
print(s1.printarea())
##########################################################################################


