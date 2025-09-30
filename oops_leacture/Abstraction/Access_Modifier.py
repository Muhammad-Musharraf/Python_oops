# -->public  --->private   ---->protected
class student:
    def __init__(self,name,roll_no,age):

        self.name=name # Public Instance Variable
        self._roll_no= roll_no # Protected Instance Variable
        self.__age=age # Private Instance Variable

    def __display(self):
        print(f"My name is {self.name} and my roll number is {self._roll_no} and my age is {self.__age}")
    
    def privatedatadisplay(self):
        self.__display()
class branch(student):
    def show(self):
        print(f" My roll no is {self._roll_no} ") 
        # derived class only access proctected  not private

# call outside the function
# def show():
#     b1=branch("Talha",53)
#     print(b1.name,b1._roll_no)

#show()
"""
Private Attributes can Acess two methods
 1) Name Mangling:- Name mangling in Python is a technique used to make class 
 attributes private by changing their names internally 
 Syntax:
 _ClassName__AttributeName
 
 2) private attributes can be used through Methods 

"""
s1=student("Aliyan",45,20)
print(s1.__dict__)
s1.__age=25 #You're not changing the private __age.You're creating a new public attribute named __age on the object s1.
#print(s1.__age)

print(s1._student__age) # name mangling and it show private attributes does not change

#print(s1.__display)  can not Access Beacause it is private method

print(s1.privatedatadisplay()) # it print private method

s1._student__display()# name mangling through method and access private method 


b1=branch("Talha",53,35)
print(b1.name,b1._roll_no)
print(b1.show())

#print(s1.__age) # Error it can not be dicect access

# s2=student("faiq",25)
# s2.display()
# s2._roll_no=35
# print(s2._roll_no)
# s2.display()