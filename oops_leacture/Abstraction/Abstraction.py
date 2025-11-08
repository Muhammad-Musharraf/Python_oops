'''
Abstraction:
Data abstraction means showing only the essential features and hiding the complex internal details.

Technically, in Python abstraction is used to hide the implementation details from the user and exposeonly 
necessary parts, making the code simpler and easier to interact with.

Ex:
A smartphone is a great real-life example of data abstraction you can make calls or take photos
 without knowing how signals or storage work. Only essential features are shown, complex details are hidden.

1)Abstract Base Class ---> its  from abc import ABC ,abstractmethod---->both abstract base class & abstract method
2)AbstractMethod ----> a method which is compusory to used in child class  

'''
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
        self.length =  float(input("Enter the Length of the Rectangle... "))
        self.width = float(input("Enter the Width of the Rectangle.... "))
        

    def printarea(self):  # Implement the abstract method
        return f"The Area of rectangle is {self.length * self.width}"
    
class circle(Shape):
    def __init__(self):
        self.radius = float(input("Enter the Radius of the Circle... "))

    def printarea(self): # if I write a Abstract method .it is coumpusory to write in Every child class
        return f"The Area of Circle is {float(math.pi*self.radius**2)}"
        
class Squre(Shape):
    def __init__(self):
        self.length = float(input("Enter the Length of the Squre... "))
        self.width = float(input("Enter the Width of the Squre... "))

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


