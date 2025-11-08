"""
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.

"""
class number:
    def __init__(self,n,m):
        self.n=n
        self.m=m


    def is_multiple(self):
        if self.m==0:
            print("Can not be divided by zero")
        elif self.n == self.m:
            print("True")
        elif self.n%self.m==0:
            print(True)
        else:
            print("N is not Multiple of M")

# Objects
n1=number(3,2)
n1.is_multiple()

"""
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.

"""
class Even_odd:
    def __init__(self,k):
        self.k=k

    def is_even(self):
        if self.k & 1==0:
            print("True")
        else:
            print("False")
         
E1=Even_odd(3)
E1.is_even()

"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.

"""
class find_min_max:
    def __init__(self,data):
        self.data=data

    def add(self,new_data):
        self.data.append(new_data)
        return new_data
    
    def min_max(self):
        smallest=self.data[0]
        largest=self.data[0]
        for value in self.data:
            if value < smallest:
                smallest=value

            elif value> largest:
                largest=value

        return f"(Smallest: {smallest}, Largest: {largest})"

n1=find_min_max([1,4,6,8,12,3,2])
print(n1.min_max())



"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.

"""




"""
Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python's comprehension syntax and the built-in sum function.
"""
class number:
    def __init__(self,n):
        self._n=n

    @property
    def n(self):
        return self._n
    @n.setter
    def n(self,new_n):
        if not isinstance(new_n,int):
            raise ValueError("must be integer")

        if new_n<=0:
            raise ValueError("N MUST BE POSITIVE")
        self._n=new_n
    def sum_of_square(self):
        total=0
        for i in range(1,self._n+1):
            total+=(i*i)
            

        print(total)
    
n1=number(4)
n1.n=5
n1.sum_of_square()














"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""
class Number:
    def __init__(self,n):
        self._n=n
        if not isinstance(n, int):
            raise TypeError("must be integer")

    @property
    def n(self):
        return self._n
    @n.setter
    def n(self,new_n):
        if not isinstance(new_n, int):
            raise ValueError("must be integer")

        if new_n<=0:
            raise ValueError("N MUST BE POSITIVE")
        self._n=new_n
    def sum_of_odd_square(self):
        
        total=0
        for i in range(1,self._n+1):
            if i%2==1:
                total+=i*i

        print(total)
    
n1=Number(4)

n1.sum_of_odd_square()
"""
What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""
class parameter:
    def __init__(self,start,stop=None,step=1):
        self.start=start
        self.stop=stop
        self.step=step
    def display(self):
        if self.stop is None:
            self.stop=self.start
            self.start=0
        if self.step==0:
            raise ValueError("step can not be zero")
        
    # Positive step logic
    
    def my_range(self):
        self.display()
        result=[]
        if self.step>0:
            current=self.start
            while current<self.stop:
                result.append(current)

                current+=self.step

        # Negative step logic

        else:
            current=self.start
            while current>self.stop:
                result.append(current)
                current+=self.step
        return result
    def show(self):
        print(f"Start: {self.start} Stop:{self.stop} step:{self.step} ")
    
p1=parameter(50,90,10)
p1.show()
print(p1.my_range())

"""  
What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, -2, -4, -6, -8?
"""      
class parameter:
    def __init__(self,start,stop=None,step=1):
        self.start=start
        self.stop=stop
        self.step=step
    def display(self):
        if self.stop is None:
            self.stop=self.start
            self.start=0
        if self.step==0:
            raise ValueError("step can not be zero")
        
    # Positive step logic
    
    def my_range(self):
        self.display()
        result=[]
        if self.step>0:
            current=self.start
            while current<self.stop:
                result.append(current)

                current+=self.step

        # Negative step logic

        else:
            current=self.start
            while current>self.stop:
                result.append(current)
                current+=self.step
        return result
    def show(self):
        print(f"Start: {self.start} Stop:{self.stop} step:{self.step} ")
    
p1=parameter(8,-9,-2)
p1.show()
print(p1.my_range())

"""
Demonstrate how to use Python's list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""



class parameter:
    def __init__(self,start,stop=None,step=1):
        self.start=start
        self.stop=stop
        self.step=step
    def display(self):
        if self.stop is None:
            self.stop=self.start
            self.start=0
        if self.step==0:
            raise ValueError("step can not be zero")
        
    
    def my_range(self):
        self.display()
        result=[]
    #Positive step logic

        if self.step>0:
            current=self.start
            while current<self.stop:
                result.append(2**current)

                current+=self.step

        # Negative step logic

        else:
            current=self.start
            while current>self.stop:
                result.append(2**current)
                current+=self.step
        return result
    def show(self):
        print(f"Start: {self.start} Stop:{self.stop} step:{self.step} ")
    
p1=parameter(9)
p1.show()
print(p1.my_range())

"""
Python's random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module in-
cludes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.

"""

import random
class choice_item:
    def __init__(self,data):
        self.data=data

    def random_choice(self):
        if len(self.data)==0:
            raise ValueError("can not Empty list ")
        index=random.randrange(len(self.data))
        return self.data[index]
r1=choice_item(["Mango","Apple","PineApple","Cherry","Watermelon","Strawberry"])
print(r1.random_choice())
        
