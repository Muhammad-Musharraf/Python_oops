class Student:
    name = "Urooj Wadood"
    Location = "General store"
s1 = Student()
print(s1.name)
print(s1.Location)   
 
s2 =Student()


class Car:
    Name = "KIA Motors"
    Model = "Sportage"
    year ="2024"

c1 = Car()
print(c1.Name)   
print(c1.Model) 
print(c1.year)

class Student:
    # #default Constructor
    # def __init__(self):
    #pass
  
      #parameterized Constructor  
    def __init__(self,name, Marks):
        self.name = name
        self.Marks = Marks
        print("adding new Student of Database...")
   
s1 = Student("Saleem",57)
print(s1.name, s1.Marks)

s2 =Student("waleed",99)
print(s2.name, s2.Marks)

s3 =Student("Urooj",85)
print(s3.name,s3.Marks)

class Student:
  name= "Musharraf"

s1=Student()
print(s1.name)

s2=Student()
print(s2.name)

class Car:
  color="Blue"
  brand="B.M.W"
  
c1= Car()
print(c1.color)  
print(c1.brand)  

class Student:
  college_name = "Formen College" # class Arttibutes
  name = "Anonymous"
  # default constructor
  # def __init__(self):
  #   print("Hello world")
  
  # parameterized construtor
  def __init__(self,name,marks):
    self.name = name # obj attribute ( obj attr > class attr)
    self.marks= marks
    print("adding new students in database..........")
  def info(self):
    print(f"Congratulation {self.name} is to get a {self.marks} Marks....")

s1=Student("karan",89)
print(s1.name,s1.marks)

s1.info()

s2=Student("Aliyan_Khalid",98)
print(s2.name,s2.marks)
s2.info()
s3=Student("Usman_Khan",86)
print(s3.name,s3.marks)
s3.info()
print(Student.college_name) # call from class 
print(s3.college_name) # call from obj both are correct 

class Teacher:
  @staticmethod
  def google():
    print("Facebook")
  def __init__(self,name,sub,marks):
    self.name = name
    self.sub = sub
    self.marks = marks
    
 
  def display(self):
      print(f"your teacher name is {self.name}")
      print(f"& he/she is Teaching {self.sub} Subjects")
  def get_sub(self):
    return self.marks
     
      
  def hello(self):
    print(f"""Hello miss/sir {self.name} you appointed as a teaacher & your are selected  a {self.sub} subjects. Thanks for providing a service 
          of teaching""")
    
t1= Teacher("Tahira_khan","Urdu",92)
print("your teching test score is ",t1.get_sub())
t1.display()
t1.hello()
t2=Teacher("Anwer","Mathematics",54)
print("your teching test score is ",t2.get_sub())

t2.display()
t2.hello()
t2.google()
