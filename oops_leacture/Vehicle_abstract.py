from vehicle_main import Vehicle

class bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.no_of_tyre=n
        self.color=color

    def start(self):
        print("Start With Kick")
    def display(self):
        print(f" My Bike color is {self.color}")

class car(Vehicle):
    def __init__(self,n,x):
        self.grear=6
        super().__init__(n)
        self.no_of_tyre=n
    def start(self):
        print("Start With key")

class Scoty(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color=color
        
    def start(self):
        print("Start With self")


