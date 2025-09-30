# Practice Question------
# Q: Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average?
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum=0
        for var in self.marks:
            sum+=var 
        print(f"hi {self.name }, your avg marks is " , {sum/3})
        
s1= Student("Musharraf",[89,70,83])
#print(s1.name)
s1.get_avg()
s1.name="Ironman"
s1.get_avg()
         
 # Create Account class with 2 attributes - balance & account no.Create methods for debit, credit & printing the balance.   
        
class Account:
   
    def __init__(self):
        self.balance =int(input("enter the balance Amount"))
        self.Acc_num =int(input("Enter your account number"))
    @staticmethod
    def veiw():
        check=input("Choose anyone card that is debit or credit")
        if check=="debit card":
            debit()
        elif check=="credit card":
            credit()
    
    
    
    def debit(self):
        d=int(input("how much amount you want to debit"))
        a= self.balance-d
        print("your remaining balance amount is : ", a)
        
    def credit(self):
        c= int(input("Enter the amount you credit....."))
        b = self.balance-c
        print("your remaining balance amount is : ",b)
        
acc1= Account()

veiw()

debit()
credit()

        
            