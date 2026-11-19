
prices = {"apple": 50, "milk": 30, "bread": 40}
stock = {"apple": 10, "milk": 5, "bread": 8}
cart = {}    # abhi khaali


def show_products():
    print("\n--- Products ---")
    for name in prices:
        print(name, "- Rs", prices[name], "- left:", stock[name])


def add_item():
    name = input("Item name: ").lower()

    if name not in prices:
        print("This item is not available")
    else:
        quantity = int(input("How many: "))

        already_in_cart = 0
        if name in cart:
            already_in_cart = cart[name]

        # Bonus: stock check
        if already_in_cart + quantity > stock[name]:
            print("Not enough stock. Only", stock[name], "left")
        else:
            cart[name] = already_in_cart + quantity
            print(name, "added to cart")


def remove_item():
    name = input("Which item to remove: ").lower()

    if name in cart:
        del cart[name]
        print(name, "removed from cart")
    else:
        print("This item is not in the cart")


def calculate_total():
    total = 0
    for name in cart:
        total = total + prices[name] * cart[name]
    return total


def calculate_discount(total):
    if total >= 1000:
        return total * 10 / 100    # 10% discount
    elif total >= 500:
        return total * 5 / 100     # 5% discount
    else:
        return 0


def print_bill():
    if len(cart) == 0:
        print("Cart is empty")
    else:
        print("\n========== BILL ==========")
        for name in cart:
            quantity = cart[name]
            price = prices[name]
            cost = price * quantity
            print(name, ":", quantity, "x", price, "=", cost)

        total = calculate_total()
        discount = calculate_discount(total)
        final_amount = total - discount

        print("--------------------------")
        print("Total    :", total)
        print("Discount :", discount)
        print("Pay      :", final_amount)
        print("==========================")



choice = ""

while choice != "5":
    print("\n1. Show products")
    print("2. Add item")
    print("3. Remove item")
    print("4. Print bill")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        show_products()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        print_bill()
    elif choice == "5":
        print("Thank you! Visit again")
    else:
        print("Wrong choice, enter 1 to 5")