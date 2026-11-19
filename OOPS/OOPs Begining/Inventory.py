# 13. Write a Python program to create a class called "Inventory" with a collection of products and methods to add and remove products, and to check for low inventory.

class Inventory:
    def __init__(self,id,title,price):
        self.__id = id
        self.__title = title
        self.__price = price
    def add_prod(self,product):
        product.append(self)
    def remove_prod(self,product):
        if self in product:
            product.remove(self)
            print("Product Removed Successfully")
        else:
            print("Product Not Found")
    def check_prod(self,product):
        if len(product)<2:
            print("Inventory Is Low")
        else:
            print("Inventory is Sufficent")
    
    def details_prod(self):
        print(f"Product Id = {self.__id}")
        print(f"Product Title = {self.__title}")
        print(f"Product Price = {self.__price}")
product = []
p1 = Inventory("ABC12","Maggie",50)
p2 = Inventory("Ma42w","Cream",10)
p3 = Inventory("Jkl21","Biscuit",20)

p1.add_prod(product)
p2.add_prod(product)
p3.add_prod(product)


print("Before Removing Product:")
for products in product:
    products.details_prod()
    print()
p1.remove_prod(product)

print("After Removing:")
for products in product:
    products.details_prod()
    print()
