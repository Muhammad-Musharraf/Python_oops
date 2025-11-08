# classmethod as alternative constuctor 

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod

    def from_string(cls,data):
        name,age = data.split("-")

        return cls(name,int(age))
    
s1=person("Ali",20)

print(s1.name,s1.age)


s2=person.from_string("Salman-23")

print(s2.name,s2.age)

#########################################################################

class Date:
    def __init__(self,day,month,year):
        self.Day=day
        self.Month=month

        self.Year=year

    @classmethod
    def fromstring(cls,data_str):

        d,m,y=map(int,data_str.split("-"))


        return cls(int(d,m,y))
    

d1=Date(2,10,2025)
d2=Date.fromstring("08-12-2030")

print(d1.__dict__)

print(d2.__dict__)
    
####################################################################

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fromdict(cls,data):

        return cls(data['name'],data['salary']) # if data in dictionary form {'name':"abc",'salary';xxxxx}
    

e1=Employee('wahab',35000)
print(e1.name,e1.salary)

# print(e1.__dict__)

emp_data={"name":"Saleem","salary": 20000}
e2=Employee.fromdict(emp_data)
print(e2.name,e2.salary)










