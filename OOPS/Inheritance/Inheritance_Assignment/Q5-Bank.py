# 5. Banking System

# Parent:
# BankAccount

# Child:
# SavingsAccount
# CurrentAccount

# Implement withdrawal rules.

class Bank_Ac:
    def __init__(self,acc_no,name,amt):
        self.__acc_no = acc_no
        self.__name = name
        self.__amt = amt

    def withdraw(Self):
        pass
    def __str__(self):
        pass
        
class SavingsAccount(Bank_Ac):
    def __init__(self,acc_no,name,amt):
        super().__init__(acc_no,name,amt)
    def withdraw(Self):
        withdraw_amt = float(input("Enter Amount You want Withdraw"))
        print(f"Your Withdraw Amount - {withdraw_amt}")
        if withdraw_amt <= 0:
            print("Invalid Withdraw Amount")
        
        elif withdraw_amt > amt:
            excess_withdraw_amt = withdraw_amt - amt
            print(f"Your withdraw Amount is more as compare to {amt},\n The Excess Withdraw Amount is {excess_withdraw_amt} ")
        else : 
            amt = amt - withdraw_amt
            print("Withdraw Successfull")
        
        
    def display_details(self):
        print(f"Your Account Type Is Saving Account")
        print(f"Your Account Number - {self.__acc_no}")
        print(f"Your Name - {self.__name}")
        print(f"Your Total Balance - {self.__amt}")


class CurrentAccount(Bank_Ac):
    def __init__(self,acc_no,name,amt):
        super().__init__(acc_no,name,amt)




        
class CurrentAccount(Bank_Ac):



