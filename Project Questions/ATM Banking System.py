# 3. ATM Banking Simulator
# Beginner–Intermediate
# Concepts: Nested conditions, loops, functions
# Requirements
# •	Verify a PIN.
# •	Display balance, deposit, withdrawal, and exit options.
# •	Prevent withdrawals exceeding the available balance.
# •	Reject invalid amounts.
# •	Use separate functions for deposit, withdrawal, and balance enquiry.
# Bonus: Allow only three PIN attempts.

def show_display(current_balance):
    print(f"show Current Balance: {current_balance}")

def deposit(current_balance):
    deposit_amt = float(input("Enter a Deposit Amount = "))
    if deposit_amt <= 0:
        print("Invalid amount")
        return current_balance
    new_balance = current_balance + deposit_amt
    return new_balance

def withdrawal(current_balance):
    withdraw_amt = float(input("enter withdraw amount = "))
    if withdraw_amt <= 0:
        print("Invalid amount")
        return current_balance
    if withdraw_amt <= current_balance:
        new_balance = current_balance - withdraw_amt
        print("You Choose Withdrawing Amount")
        return new_balance
    else:
        print("Sorry your Balance is low")
        return current_balance


current_balance = float(input("Enter Your Current Balance Amount = "))
pin = 1234
attemps = 0
Authentication = False
while attemps<3:
    user_password = int(input(" enter password ="))
    if user_password==pin:
        print("acess Granted")
        Authentication = True
        break
    else:
        attemps+=1
        print(f"Incorrect Password Attemp left {3-attemps}")

if not Authentication:
    print("Card Blocked, too many wrong attempts")

while Authentication:
    print("menu")
    print("1 for Balance display")
    print("2 for Deposit")
    print("3 for Withdrawal")
    print("4 for exit")

    choice = int(input("Enter a Choice (1-4) = "))
    if choice == 1:
        show_display(current_balance)
    elif choice == 2:
        current_balance = deposit(current_balance)
    elif choice == 3:
        current_balance = withdrawal(current_balance)
    elif choice == 4:
        print("Thank you, Goodbye")
        break
    else:
        print("Wrong choice, try again")













