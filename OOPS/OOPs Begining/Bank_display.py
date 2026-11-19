# Bank Account
# Create a class BankAccount with fields: accountNumber, holderName, balance.
# Use setters to assign values. Add a method to display balance.


class Bank:
    def __init__(self,acc_no,holder_name,balance):
        self.__acc_no = acc_no
        self.__holder_name = holder_name
        self.__balance = balance

    def display_balance(self):
        print(f"Welcome , {self.__holder_name}")
        print(f"Your Account Number is : {self.__acc_no}")
        print(f"Your Balace is : {self.__balance}")

cus_1 = Bank(101290,"Farhan",102000)
cus_2 = Bank(102224,"Ali",202032)
cus_3 = Bank(102442,"Lela",211110)

cus_1.display_balance()
print()
cus_2.display_balance()
print()
cus_3.display_balance()








