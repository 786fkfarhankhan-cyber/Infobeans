# 3. Online Shopping Cart , Create a shopping cart system.

# A cart should:
# store customer name
# maintain list of products
# maintain total bill
# Functionalities
# Add product
# Remove product
# Calculate final amount
# Apply discount using static method
# Track total carts created
# Concepts Practiced
# list inside object
# object interaction
# static method
# class variable

 
class ShoppingCart:
    __cart_count = 0
 
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.__products = []
        self.__total_bill = 0
        ShoppingCart.__cart_count += 1
 
    def add_product(self, name, price):
        if price > 0:
            self.__products.append([name, price])
            self.__total_bill += price
            print(name, "added")
        else:
            print("Invalid price")
 
    def remove_product(self, name):
        for product in self.__products:
            if product[0] == name:
                self.__products.remove(product)
                self.__total_bill -= product[1]
                print(name, "removed")
                return
        print("Product not found")
 
    def calculate_bill(self):
        return self.__total_bill
 
    @staticmethod
    def apply_discount(amount, discount):
        if amount >= 0 and 0 <= discount <= 100:
            return amount - (amount * discount / 100)
        else:
            print("Invalid amount or discount")
            return amount
 
    def display_cart(self):
        print("Customer:", self.__customer_name)
        print("Products:", self.__products)
        print("Total Bill:", self.__total_bill)
 
    @classmethod
    def get_cart_count(cls):
        return cls.__cart_count
 
 
cart1 = ShoppingCart("Farhan")
cart1.add_product("Laptop", 50000)
cart1.add_product("Mouse", 500)
cart1.display_cart()
final_amount = ShoppingCart.apply_discount(cart1.calculate_bill(), 10)
print("Final amount after discount:", final_amount)

