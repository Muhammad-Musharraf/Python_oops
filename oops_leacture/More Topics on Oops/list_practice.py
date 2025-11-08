class Student:
    def __init__(self,name:str,age:int,Seat_no:int,capacity: int=6):
        self._name=name
        self._age=age
        self._Seat_no=Seat_no
        self._capacity= capacity
        self._index=0
        self._size=0
        self._course= [None] * self._capacity


    def add_course(self,new_course):
        if self._index>self._capacity:
            raise OverflowError("Cannot add more courses — capacity reached")
        self._course[self._index]=new_course
        self._index+=1

    

    
    @property
    def Seat_no(self):
        return self._Seat_no
    
    @Seat_no.setter
    def Seat_no(self,update_seat):
        if not isinstance(update_seat,int):
            raise TypeError("MUST BE INTEGERS")
        self._Seat_no=update_seat
        


    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,new_age):
        self._age=new_age
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        

        if not isinstance(new_name,str):
            raise TypeError("MUST BE STRING")
        self._name=new_name
    
        
    def __str__(self):
        return f""" 
            NAME:{self._name}
            SEAT # {self._Seat_no}
            Courses: {', '.join([str(c) for c in self._course if c])}
            AGE: {self._age}
          
        """