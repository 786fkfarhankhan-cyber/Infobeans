# 4. Restaurant Billing System
# Beginner–Intermediate
# Concepts: Loops, conditions, functions
# Requirements
# •	Display a menu with item prices.
# •	Let customers select items and quantities.
# •	Calculate the running bill.
# •	Apply discounts based on the bill amount.
# •	Calculate the final bill, including tax.
# Bonus: Add coupon codes and repeat-order functionality.




def calculate_final_bill(bill):
    # Discount
    if bill >= 1000:
        discount = bill * 0.10
    elif bill >= 500:
        discount = bill * 0.05
    else:
        discount = 0

    after_discount = bill - discount
    tax = after_discount * 0.05
    final_bill = after_discount + tax

    print("Total:", bill)
    print("Discount:", discount)
    print("Tax:", tax)
    print("Final Bill:", final_bill)


print("1. Pizza  - 200")
print("2. Burger - 100")
print("3. Coffee - 50")
print("4. Done")

bill = 0

while True:
    choice = input("Choose item (1-4): ")

    if choice == "4":
        break

    if choice == "1":
        price = 200
        print("You chose Pizza")
    elif choice == "2":
        price = 100
        print("You chose Burger")
    elif choice == "3":
        price = 50
        print("You chose Coffee")
    else:
        print("Invalid choice!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity!")
    else:
        bill = bill + price * quantity
        print("Running bill:", bill)

print("\n--- FINAL BILL ---")
calculate_final_bill(bill)














