# Product Inventory
# Create a class Product with fields: productId, name, quantity, price.
# Use setters to assign values. Add a method to calculate total value (quantity * price).

class Product_inventory:
    
    def __init__(self):
        self.__product_id = None
        self.__name = None
        self.__quantity = None
        self.__price = None
        
    def set_product_id(self,product_id):
        self.__product_id = product_id
    def set_name(self,product_name):
            self.__name = product_name
    def set_quantity(self,product_quantity):
            self.__quantity = product_quantity
    def set_price(self,product_price):
        self.__price = product_price 

    def product_details(self):
        print(f"Product Id = {self.__product_id} \nProduct Name = {self.__name} \nProduct Quantity = {self.__quantity} \nProduct Price = {self.__price}")   


product_1 = Product_inventory()
product_1.set_product_id(101)
product_1.set_name("Shoes")
product_1.set_quantity(4)
product_1.set_price(2000)
product_1.product_details()


print("By Input")
id = int(input("Enter a Product Id = "))
name = input("Enter a Product Name = ")
quan = int(input("Enter a Product Quantity = "))
price = int(input("Enter a Product Price = "))
print()

product_2 = Product_inventory()
product_2.set_product_id(id)
product_2.set_name(name)
product_2.set_quantity(quan)
product_2.set_price(price)
product_2.product_details()


