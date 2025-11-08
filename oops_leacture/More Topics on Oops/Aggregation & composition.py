# Aggregation = Represents a relationship where one object (the whole)
# contains references to one or more INDEPENDENT objects (the parts)

class Library:
    def __init__(self,name):
        self.name=name
        self.Books=[]

    def add_book(self,book):
        self.Books.append(book)

    
    def list_book(self):
        return [f"{books.title} by {books.aurthor}" for books in self.Books ]





class Book:
    def __init__(self,title,aurthor):
        self.title=title
        self.aurthor=aurthor

libaray=Library('Ghalib Library Nazimabad')
print(libaray.name)

book1=Book('The Odyssey','Homer')

book2=Book('Harry Potter series','J.K. Rowling')

book3=Book('Rich Dad Poor Dad','Robert Kiyosaki')

libaray.add_book(book1)
libaray.add_book(book2)
libaray.add_book(book3)
# print(libaray.list_book())

for book in libaray.list_book():
    print(book)

#############################################
'''
Question:
Create two classes — Student and Department.
A Department can have many Student objects (aggregation).
Write a program that:

Creates a Department object.

Adds multiple Student objects to it.

Displays all students belonging to that department.

'''
class Student:
    def __init__(self,Seat_no,Name):
        self.Seat_no=Seat_no
        self.Name=Name


class department:
    def __init__(self,depart_name):
        self.depart_name=depart_name
        self.name=[]

    def add_student(self,Names):
        self.name.append(Names)

    def list_student(self):
        return [f"{name.Name}"for name in self.name]




d1=department("Computer Science ")
print(d1.depart_name)

s1=Student(424016673,'Ali')
s2=Student(82456789,'Amin')
s3=Student(524016673,'yamin')
s4=Student(224016673,'Muneer')

d1.add_student(s1)

d1.add_student(s2)
d1.add_student(s3)
d1.add_student(s4)


#print(d1.list_student())

for student in d1.list_student():
    print(student)



################################################
'''
Composition = The composed object directly owns its components, which cannot exist independently
"owns-a" relationship

'''
class Engine:
    def __init__(self,horse_power):
        self.horse_power=horse_power

    
class Wheel:
    def __init__(self,size):
        self.size=size


class Car:
    def __init__(self,make, model, horse_power,wheel_size):
        self.make=make
        self.model=model
        self.engine=Engine(horse_power)
        self.wheels=[Wheel(wheel_size) for wheel in range(4)]

    def show(self):
        return f'{self.make} {self.model} {self.engine.horse_power}hp {self.wheels[0].size} inch'



car1=Car(make='Toyota',model='M500',horse_power=1600,wheel_size=18)

car2=Car(make='Kia',model='Spotage',horse_power=2000,wheel_size=16)

print(car1.show())
print(car2.show())


    

        


        



    

        