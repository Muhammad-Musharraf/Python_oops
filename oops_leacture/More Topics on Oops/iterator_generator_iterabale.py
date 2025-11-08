import sys
def creator1():
    i=1

    while i<=200:
        yield i

        i+=1
print(creator1())
x=creator1()

print(next(x))
print(next(x))
print(next(x))
print(list(x))

z=sys.getsizeof(x)
print(z)

print([num+10 for num in creator1()])
##################################################################


def gen(n):

    for i in range(n):
        yield i

obj=gen(4)

# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

num=[100,1,2,3,4]

iter1=iter(num)

# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# # print(next(iter1))
# # print(next(iter1))

# for i in num:
#     print(i)

################################
# FOR LOOP IN OOPS STYLE------> __iter__ & __next__

class counter:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self # returns the iterator object itself
    
    def __next__(self):
        if self.start>self.end:
            raise StopIteration
        
        value=self.start

        self.start+=1
        return value
    
for num in counter(1,4):
    print(num)
#####################################################
class even_number:
    def __init__(self,limit):
        self.limit=limit
        self.num=0

    def __iter__(self):
        return self

    def __next__(self):
        self.num+=2

        if self.num>self.limit:
            raise StopIteration

        return self.num

even =even_number(10)
for i in even:
    print(i)

################################################

# Example 3: Reverse String Iterator
class reverse_string:
    def __init__(self,text):
        self.text=text
        self.index=len(text)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index-=1

        return self.text[self.index]

s1=reverse_string('Python')
# iterator=iter(s1)
print(next(s1))
print(next(s1))
print(next(s1))



# for chr in s1:
#     print(chr)

######################################
# GERNATOR IN OOPS STYLE----->  yield


class number_series:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def generate_num(self):
        for i in range(self.start,self.end+1):
            yield i


# if you want to print all number
n1=number_series(1,4)
for i in n1.generate_num():
    print(i)



# if you want to generate one by one number used generator
# num1=n1.generate_num()

# iterator=iter(num1)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

##################################
# Example 2---->  Generator for Filtering

class Employee:
    def __init__(self,employee):
        self.employee=employee


    def get_high_salary(self,thesold):

        for emp in self.employee:
            if emp['salary']>thesold:
                yield emp


data = [
    {'name': 'Ali', 'salary': 170000},
    {'name': 'Sara', 'salary': 95000},
    {'name': 'Talha', 'salary': 57000}
]
e1=Employee(data)
it=iter(e1.get_high_salary(80000))
print(next(it))
print(next(it))
# print(next(it)) if you check & filter one by one 


# for i in e1.get_high_salary(50000):
#     print(i)


# Example #3 
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

c1=Countdown(5)
it=iter(c1)
print(next(it)) # only 5 

for i in it: # 4---->0
    print(i)


# for i in Countdown(5):
#     print(i)



    


    




