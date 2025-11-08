class Change_Calculator:
    def __init__(self,charged_Amount,given_Amount):
        self.charged_Amount=charged_Amount
        self.given_Amount=given_Amount
        self.denoimations=[5000,1000,500,100,50,20,10,5,2,1]

    def cal_change(self):
        if self.given_Amount<self.charged_Amount:
            raise ValueError("Given Amount is greater than Charged Amount")
        change=self.given_Amount-self.charged_Amount
        print(f"\nTotal Change to return: {change}")

        change=int(change)

        change_breakdown={}


        for denomination in self.denoimations:
            count=change//denomination
            change_breakdown[denomination]=count
            change%=denomination
        return change_breakdown
    
    def display(self):
        breakdown=self.cal_change()

        for denomination, count in breakdown.items():
            if count>0:
                notes_or_coin="$" if denomination >=10 else "cent"
                print(f"{count} is  of {denomination} {notes_or_coin}")

        return breakdown

c1=Change_Calculator(2000,4855)
c1.display()







