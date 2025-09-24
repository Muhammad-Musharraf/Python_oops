from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyres = n

    @abstractmethod
    def start(self): # Abstract Method
        pass
    def display(self): # concreate method
        print("Hey I am Calling from Vehicle class ")

        
