"""
Inheritance:
When one class(child/derived) derives the properties & methods of another class(parent/base).

Inheritance is a fundamental concept in object-oriented programming (OOP) 
that allows a class (called a child or derived class) to inherit attributes and 
methods from another class (called a parent or base class). 




Syantax
'class car:   ----> Parents/base Class

class Toyota(car):  ----> Clild/derived  class

"""
class Car:
    color="Black"

    @staticmethod
    def start():
        print("Start Car....")

    @staticmethod
    def stop():
        print("Stop Car....")

class Toyota(Car):
    def __init__(self,name):
        self.name=name

car1=Toyota("Fortunre")
car2=Toyota("Civic")
print(car2.name,car2.color)
print(car1.name,car1.color)
print(car1.start())
print(car1.stop())
###########
"""
Types of Inheritance
---->Single Inheritance
---->Multi-level Inheritance
---->Multiple Inheritance
----> Hierarchical Inheritance
---->Hybrid Inheritance

"""
# Single Inheritance: In single inheritance, a child class inherits from just one parent class.
# Example of single inheritance
class Animal:
    def __init__(self,name):
        self.name=name

    def info(self):
        print(f"Animal Name: {self.name}")
class Dog(Animal):
    def sound(self):
        print(self.name,"Barks")

dog1=Dog("BoB")
print(dog1.info())
print(dog1.sound())

#Multi-level Inheritance:In multilevel inheritance, a class is derived from another derived class (like a chain).
#Example of Multi-level Inheritance:
class Car:
    color="Black"

    @staticmethod
    def start():
        print("Start Car....")

    @staticmethod
    def stop():
        print("Stop Car....")

class Toyota(Car):
    def __init__(self,brand):
        self.brand=brand

class fortunre(Toyota):
    def __init__(self, Type,brand):
        #Toyota.__init__(self,brand)
        super().__init__(brand)
        self.brand=brand
        self.Type=Type


car1=fortunre("Eletric","Revo")
print(car1.start())
print(car1.Type)
print(car1.brand)
print(car1.stop())

# Multiple Inheritance -----> In multiple inheritance, a child class can inherit from more than one parent class.
# Example:This example demonstrates Employee inheriting properties from two parent classes: Person and Job.
class person:
    def __init__(self,name):
        self.name=name
class job:
    def __init__(self,salary):
        self.salary=salary

class Employee(person,job): # Inherits from both Person and Job

    def __init__(self, name,salary):
        person.__init__(self,name)
        job.__init__(self,salary)

e1=Employee("Musharraf",100000)
print(e1.name,e1.salary)

e2=Employee("Talha",1000000)
print(e2.name,e2.salary)
# 2nd Simple Example
class A:
    var_a="Welcome to Class A"
class B:
    var_b="Welcome to Class B"
class C(A,B):
    var_c="Welcome to Class A"

var=C()
print(var.var_a)
print(var.var_b)
print(var.var_c)
print("\n")

"""
Super Method:-
super() method is used to access methods of the parents class

In Python, the super() function is used to call methods from a parent (superclass) inside a child (subclass). It allows you to extend or override inherited methods while still reusing the parent’s functionality.

Syntax:
super()

"""
class data:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def ads(self):
        print(f"My World Best Brand is {self.name}")


class fun(data):
    def __init__(self, id, name,email):
        super().__init__(id, name) # super can access parents class arributes
        super().ads() # super can access parents class methods. if i try to print every object used this method 
        self.email=email


obj1=fun("1001","Olivia","olivia@gmail.com")
print(obj1.id,obj1.name,obj1.email)


obj2=fun("1002","SunLight","sunlight@gmail.com")
print(obj2.id,obj2.name,obj2.email)
# Hybrid Inheritance: Hybrid inheritance is a combination of more than one type of inheritance.
# Example
class Person:
    def __init__(self,name):
        self.name=name

class Employee(person):# Single Inheritence
    def role(self):
        print(f"{self.name} is a employee...")

class Project:
    def __init__(self,project_name):# multiple Inheritence
        self.project_name=project_name

class Team_Lead(Employee,Project):# Hybrid Inheritence (Single inheritence + multiplr Inheritence )
    def __init__(self, name,project_name):
        Employee.__init__(self,name)
        Project.__init__(self,project_name)

    def details(self):
        print(self.name,"Leads Project",self.project_name)

#Objects        
lead=Team_Lead("Tuba Shahid","Senior Data Scientist")
print(lead.role())
print(lead.details())
        

# Hierarchical Inheritance:In hierarchical inheritance, multiple child classes inherit 
# from the same parent class.
#Example:
class person:
    def __init__(self,name):
        self.name=name

class Employee(person):
    def role(self):
        print(self.name,"Works as a Employee")

class Intern(person):
    def role(self):
        print(self.name,"is a Intern")

Emp=Employee("Musharraf")
print(Emp.role())

intern=Intern("Talha")
print(intern.role())








    





