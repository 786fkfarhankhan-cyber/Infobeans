# # 2. Bank Account Simulation
# # Problem Design a banking system using OOP.
# # Requirements
# # Each account should contain:
# # account number
# # holder name
# # balance
# # Functionalities
# # Deposit money
# # Withdraw money
# # Prevent withdrawal if balance insufficient
# # Display account summary
# # Maintain bank-wide interest rate as class variable
# # Add static method to validate minimum balance rule
# # Concepts Practiced
# # object state management
# # static methods
# # class variables
# # validations
        
class Bank:
    print("*" * 11, "Welcome Customer", "*" * 11)

    interest = 7

    def __init__(self, acc_no, holder_name, balance):
        self.__acc_no = acc_no
        self.__holder_name = holder_name
        self.__balance = balance

    def deposit_money(self, deposit_amt):
        if deposit_amt > 0:
            self.__balance = self.__balance + deposit_amt
            print("Deposit successful")
            return self.__balance
        else:
            print("Invalid Amount")

    def withdraw_money(self, withdrw_amt):
        if withdrw_amt <= 0:
            print("Invalid Withdrawal Amount")

        elif self.__balance - withdrw_amt >= 1000:
            self.__balance -= withdrw_amt
            print("Withdrawal successful")
            return self.__balance

        else:
            print("Insufficient balance or minimum balance rule violated")

    @staticmethod
    def validate_minimum_balance_rule(balance):
        return balance >= 1000

    def display(self):
        print("\n----- Account Summary -----")
        print(f"Account Number: {self.__acc_no}")
        print(f"Holder Name: {self.__holder_name}")
        print(f"Current Balance: ₹{self.__balance}")
        print(f"Interest Rate: {Bank.interest}%")

        if Bank.validate_minimum_balance_rule(self.__balance):
            print("Minimum balance maintained")
        else:
            print("Please maintain minimum balance of ₹1000")


c1 = Bank(101, "Farhan", 5000)

c1.display()
c1.deposit_money(2000)
c1.withdraw_money(3000)
c1.display()
