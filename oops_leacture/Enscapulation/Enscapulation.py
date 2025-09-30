"""
Encapulation:
    Encapsulation means hiding internal details of a class and only exposing what's necessary.
    It helps to protect important data from being changed directly and keeps the code 
    secure and organized.
    

"""
# Getter  & Setters
class Myclass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"The value is {self._value}")
    
    @property
    def ten_value(self):
        return 10* self._value
    
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10

        
     
obj=Myclass(50)

obj.ten_value=67 # setter   # error beacause they setter are not given

print(obj._value)

print(obj.show())
print(obj.ten_value)
####################################

#                      project of bank Account

class bankAccount:
    def __init__(self,Account_No,balance):
        self.__Account_No=Account_No
        self.__balance=balance
        self.deposit_money=int(input("Enter the money you deposit  "))
        self.with_draw_money=int(input("Enter the money you  with_draw "))

    @property
    def show(self):
        print(f"The Account No. is {self.__Account_No} & the balance is {self.__balance}")

    @show.setter
    def show(self,new_balance):
        if self.__balance >0:
            self.__balance=new_balance
            return self.__balance
        elif self.__balance <0:
            print("balance should be positive")
        else:
            print("invalid syntax")

    def deposit(self):
        d= input("do you want to deposit money. write yes or no ")
        if d=="yes":
            
            update_balance=self.__balance+self.deposit_money
            print(f"""The total ammount is {self.__balance}  deposited money is {self.deposit_money} and 
remaining balance is {update_balance}.\n Thanks you """)
        elif d=="no":
            return f"the curent balance is {self.__balance}"
        
        else:
            print("invalid syantax")

    def with_draw(self):
        get = input("do you want to with_draw_money. write yes or no ")
        if get=="yes":
            
            current_balance=self.__balance-self.with_draw_money
            print(f"""The total ammount is {self.__balance} with_draw ammount is {self.with_draw_money} and 
remaining balance is {current_balance}.\n Thanks you""")
        elif get=="no":
            return f"your current balance is {self.__balance} "
            
        else:
            print("invalid syantax")

        

    
b1=bankAccount("5454577",40000)
b1.show=90000
print(b1.show)
print(b1.deposit())
print(b1.with_draw())