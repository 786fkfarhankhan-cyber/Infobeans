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

pin = 1234
balance = 5000

# PIN check (3 attempts)
login = False
for i in range(3):
    entered = int(input("Enter PIN: "))
    if entered == pin:
        login = True
        break
    print("Wrong PIN!")


    
def check_balance(balance):
    print("Your balance is:", balance)


def deposit(balance):
    amount = int(input("Enter amount to deposit: "))
    if amount <= 0:
        print("Invalid amount!")
    else:
        balance = balance + amount
        print("Deposit successful.")
    return balance


def withdraw(balance):
    amount = int(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Not enough balance!")
    else:
        balance = balance - amount
        print("Take your cash.")
    return balance




# Menu
if login:
    while True:
        print("\n1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")
else:
    print("Card blocked.")















