# To map with real world scenarios, we started using objects in code.This is called object oriented programming.

# creating a class
class student:
    name="Musharraf" # class Arttibutes

# Constructor
# All classes have a function called __init__(), which is always executed when the object is being initiated.
    def __init__(self,greet,name,age):
        self.greet=greet # objects Attributes
        
        self.name=name # if class Attributes & Objects Attributes is Same so (Obj Attribute > Class Attributes)
        self.age = age

# Method
# Methods are functions that belong to objects.
    def introduction(self):
        print(f"My Name is {self.name} & my Age is {self.age}")
        

# creating Objects
s1=student("Hello","Ali",25) #instance
print(s1.greet)
print(s1.greet,s1.name)
s1.introduction()
# Q: Create student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average.
# class students:
#     def __init__(self,math,eng,chem):
#         self.math=int(input("Enter the Math Marks "))
#         self.eng=int(input("Enter the eng Marks "))
#         self.chem=int(input("Enter the chem Marks "))
        
    
#     def avg(self):
#         marks=self.math+ self.eng+ self.chem 
#         print("The average Marks of three Subjects is ",(marks/3))


#stud1=students(95,93,92)
#stud1.avg()

# 2nd Methods od this Practice Question
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(f"My Name is {self.name} and your Average Score is {sum/3}") 
    

#objects
S1 =Student("Hurain",[95,93,92])
S1.get_avg()

# Static Methods
# Methods that don’t use the self parameter (work at class level)
class person:
    def __init__(self,country):
        self.country=country

    @staticmethod   # decorator
    def college():
        print("Bharia College") # it does not allow objects parameter and it works only class level

"""
Decorators allow us to wrap another function in order to
extend the behaviour of the wrapped function, without
permanently modifying it.

"""

p1=person("Pakistan")
print(person.college())

"""
del keyword
Used to delete object properties or object itself.
 syntax
 del s1.name
 del s1    

"""
class company:
    def __init__(self,compant_name):
        self.company_name=compant_name

c1=company("Mari Energy")
print(c1.company_name)
# del c1.company_name
print(c1.company_name) # delete c1

"""
class method
A class method is bound to the class & receives the class as an implicit first argument.
---> Note - static method can't access or modify class state & generally for utility.

class Student:
    @classmethod
    def college( cls):#decorator
         pass

"""
    
class person:
    name="Umme-Abhiha"


    @classmethod
    def changename(cls,name):
        cls.name=name

    


    # def changename(self,name):
    #     self.__class__.name="Sami"

    # def changename(self,name):
#     person.name=name

p1=person()
print(p1.changename("Uzair Khan"))
print(p1.name)

print(person.name)


"""
@staticmethod------------->():
@classmethod-------------->(cls):
@instancemethod------------>(self):

"""
class boys:
    def __init__(self,math,phy,chem):
        self.math=math
        self.phy=phy
        self.chem=chem

    @property    
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+ "%"
    
    @percentage.setter
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+ "%"
    

    # def change_calc(self):
    #     self.percentage=str((self.phy+self.chem+self.math)/3)+ "%"

    

    
        
stu1=boys(98,97,95)
#print(stu1.change_calc())
print(stu1.percentage)

stu1.phy=86
print(stu1.phy)
#print(stu1.change_calc())
print(stu1.percentage)
    
    