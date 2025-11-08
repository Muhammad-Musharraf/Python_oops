class changeCalculator:
    def __init__(self,charged_amount,given_amount):
        self.__charged_amount=self._charged_amount_validator(charged_amount,given_amount)
        self.__given_amount=self._given_amount_validator(given_amount,charged_amount)
        self.__denominations=(5000,1000,500,100,50,20,10,5,1)

    @property
    def charged_amount(self):
        return self.__charged_amount
    @charged_amount.setter
    def charged_amount(self,new_charged_amount):
        self.__charged_amount=self._charged_amount_validator(new_charged_amount,self.__given_amount)

    @property
    def given_amount(self):
        return self.__given_amount
    @given_amount.setter
    def given_amount(self,new_given_amount):
        self.__given_amount=self._given_amount_validator(new_given_amount,self.__charged_amount)
    
    def _charged_amount_validator(self,charged_amount,given_amount):
        if not isinstance(charged_amount,int):
            raise TypeError("Charged Amount Must be integer")
        if charged_amount>given_amount:
            raise ValueError("Charge amount can not be greater than given amount")
        if charged_amount<0:
            raise ValueError("Charged Amount Must be Positive or Non_negative")
        return charged_amount
    def _given_amount_validator(self,given_amount,charged_amount):
        if not isinstance(given_amount,int):
            raise TypeError("Given Amount Must be integer")
        if given_amount<charged_amount:
            raise ValueError("given amount can be less than charged ammount")
        return given_amount
    
    @property
    def change(self):
        remaining_change=self.__given_amount-self.__charged_amount
        change_breakdown={}

        for denomination in self.__denominations:
            if remaining_change<1:
                break
        num_of_unit= remaining_change//denomination
        if num_of_unit> 0:
            change_breakdown[denomination]=num_of_unit
            remaining_change%=denomination

        return change_breakdown
    
    def _get_punctuation(self, current_index, keys_length):
        """
        Return a separator: comma if more items follow, else period.
        """
        # If not the last item, use a comma, otherwise a full stop
        if current_index < keys_length - 1:
            return ","
        return "."

    def _format_denomination(self, denomination, quantity):
        """
        Format a denomination into 'note' or 'coin' with its count.
        """
        # Notes are 10 or above, coins are less than 10
        phrase = f" {quantity} note/s of {denomination}"
        if denomination < 10:
            phrase = f" {quantity} coin/s of {denomination}"
        return phrase
    
    def _formet_string(self):
        change=self.change
        keys_sequence=tuple(change.keys())

        message="you Have"
        for denomination,quantity in change.items():
            message+=self._format_denomination(denomination,quantity)

            current_index=keys_sequence.index(denomination)
            message+=self._format_denomination(denomination,quantity)
        return message
    
    def display(self):
        print(self.formet_string())

    def __str__(self):
        return(
            f"Charged Amount: {self.__charged_amount}\n"
            f"Given Amount: {self.given_amount}\n"
            f"Cash Back: {self._formet_string()}"
        )

obj=changeCalculator(700,1000)
print(obj)









