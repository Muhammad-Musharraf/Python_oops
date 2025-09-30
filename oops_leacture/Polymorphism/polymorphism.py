"""
polymorphism:
    The word "polymorphism" means "many forms", and in programming it refers to
methods/functions/operators with the same name that can be executed on many objects or classes.

Topics:
1----> Duck Typing
2----> Magic/Dunder Method 
3----> Method Overriding
4----> Method Overloading
5----> Operator Overloading

"""
# Duck Typing:"" Another way to Achieve polymorhism besides inheritance Object must Have a minimum
# nessary  Attribues/Methods"
# If it looks like a duck, swims like a duck, and quacks like a duck, then it must  be a duck.

class rectangle:
    def draw(self):
        print("Shape is rectangle")

class square:
    def draw(self):
        print("Shape is Square")
class circle:
    def draw(self):
        print("Shape is Circle")

class rombus:
    def draw(self):
        print("Shape is rombus")

data=[rectangle(),square(),circle(),rombus()] # error 'rombus' object has no attribute 'draw'

for obj in data:
    obj.draw()

###############################
class Animal:
    Alive=True

class Dog(Animal):
    def sound(self):
        print("Woof Woof")
class Cat(Animal):
    def sound(self):
        print("Meow Meow")

class car: #
    Alive=True
    def sound(self):
        
        print("Honk!!")


animal= [Dog(),Cat(),car()]
for obj in animal:
    obj.sound()
    print(obj.Alive) # if error 'car' object has no attribute 'Alive'
    print("Information Displayed")
    print(" ")
#############################################
class Duck:
    def swim(self):
        print("I am  Duck I can Swim")
    def Speak(self):
        print("Quak Quak")
class Dog:
    def swim(self):
        print("I am  Dog I can Swim")
    def Speak(self):
        print("Woof Woof")

class cat:
    def swim(self):
        print("I am  Cat I can Swim")
    def Speak(self):
        print("Meow Meow")
    

def display(obj):
    obj.swim()
    obj.Speak()
    print("Information Displayed")
    print()


obj=Duck()
display(obj)

obj=Dog()
display(obj)

obj=cat()
display(obj)
"""
Magic/Dunder Method:-
Python Magic methods are the methods starting and ending with double underscores '__'.
 They are defined by built-in classes in Python and commonly used for operator overloading. 
They are also called Dunder methods, Dunder here means "Double Under (Underscores)".

"""
from emp import employee


e=employee("Harry")

print(e) #str Method
print(str(e)) #str method 
print(repr(e)) #repr Method
e() #call Method

print(len(e)) ##len Method
print(repr(e))
"""

Method Overriding:-
Method overriding is an example of run time polymorphism. 
In this, the specific implementation of the method that is already provided
 by the parent class is provided by the child class. It is used to change the 
 behavior of existing methods and there is a need for at least two classes for
method overriding. In method overriding, inheritance always required as it 
is done between parent class(superclass) and child class(child class) methods.

"""

class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class Square(Shape):
    def __init__(self,Radius):
        self.Radius=Radius
        super().__init__(Radius,Radius)

    def area(self):
        return  3.14* super().area() # method Overridding
    

s=Shape(8,5)
print(s.x)
print(s.area())
    
sq=Square(8)
print(sq.area())
####################################

class A:
    def show(self):
        print("Class is A")
    
class B(A):
    def show(self):
        print("Class is B")
        
class1=B()
class1.show()

class1=A()
class1.show()
#######################################
class FAther:
    def sleep(self):
        print("sleep from 10:00 AM to 7:00 AM")

    def Eating(self):
        print("Eating!!!")

class Son(FAther):
    def sleep(self):
        print("sleep from 02:00 AM to 10:00 AM")
        super().sleep()
    def Eating(self):
        print("I am Eating Burger")
        super().Eating()

    

son=Son()
print(son.sleep())
print(son.Eating())

"""
Method OverLoading:-
Method Overloading is an example of Compile time polymorphism. 
In this, more than one method of the same class shares the same method name 
having different signatures. Method overloading is used to add more to the 
behavior of methods and there is no need of more than one class for method overloading.

"""
class Area:
    def find_Area(self,x=None,y=None):
        if x!=None and y!=None:
            print(f"The Area of Rectangle is {x*y}")

        elif x!=None:
            print(f"The Area of Square is {x*x}")

        else:
            print("Nothing find_Area")

area=Area()
area.find_Area()
area.find_Area(2)
area.find_Area(2,4)
###############################
class Demo:
    # def Add(self,a,b,c=0):  # deafault parameter
#     return a+b+c
    
    def Add(self,*args): # *args
        total=0
        for i in args:
            total+=i
        return total
    
#if i Make a add three parameter and Already make a function of two parameter.Demo.Add() missing 1 required positional argument: 'c'
#    def Add(self,a,b,c):
#         return a+b+c
    
    
d=Demo()
print(d.Add(2,3))
print(d.Add(2,3,4))
print(d.Add(2,3,4,7,8,9))
print(d.Add(2,3,4,7,8,99,776))


# Operator Overloading
class Vector:
    #A=xi+ yj+ zk
   
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"({self.i}i+{self.j}j+{self.k}k)"

    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
    def __sub__(self,x):
        return Vector(self.i-x.i,self.j-x.j,self.k-x.k)
    
    def __mul__(self,x):
        return Vector(self.i*x.i,self.j*x.j,self.k*x.k)
    
    def __truediv__(self,x):
        return Vector(self.i/x.i,self.j/x.j,self.k/x.k)
    
    
    
    

    
    
v1=Vector(10,12,6)      
v2=Vector(2,4,2)
print(v1)
print(v2)
print(v1+v2)
print(type(v1+v2))
print(v1-v2)
print(v1*v2)
print(v1/v2)
     
