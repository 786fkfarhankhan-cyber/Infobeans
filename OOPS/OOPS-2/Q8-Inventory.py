class Product:
    def __init__(self, product_id, name, quantity, price):
        self.__product_id = product_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price
 
    def add_stock(self, quantity):
        if quantity > 0:
            self.__quantity += quantity
            print("Stock added")
        else:
            print("Invalid quantity")
 
    def purchase_stock(self, quantity):
        if quantity <= 0:
            print("Invalid quantity")
        elif quantity <= self.__quantity:
            self.__quantity -= quantity
            print("Purchase successful")
        else:
            print("Not enough stock")
 
    def inventory_value(self):
        return self.__quantity * self.__price
 
    def display(self):
        print("Product:", self.__name)
        print("Quantity:", self.__quantity)
        print("Inventory Value:", self.inventory_value())
 
 
p1 = Product(1, "Pen", 100, 10)
p1.add_stock(20)
p1.purchase_stock(30)
p1.display()
