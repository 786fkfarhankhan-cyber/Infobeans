# Mobile Phone Store
# Create a class Mobile with fields: brand, model, price.
# Use setters to set values. Create a method to check if phone is affordable (price < 20000).


class Mobile_store:
    def __init__(self):
        self.__brand = None
        self.__model = None
        self.__price = None
    def set_brand(self,brand):
        self.__brand = brand
    def set_model(self,model):
        self.__model = model
    def set_price(self,price):
        self.__price = price

    def check_affordability(self):
        return self.__price < 20000
    def display(self):
        print(f"Mobile Brand : {self.__brand}")
        print(f"Mobile Model : { self.__model}")
        print(f"Mobile Price : {self.__price}")
        if self.check_affordability():
            print("You can Afford it")
        else:
            print("You Can't Afford it")

m1 = Mobile_store()
m1.set_brand("Redmi")
m1.set_model("16 pro")
m1.set_price(55000)
m1.check_affordability()
m1.display()
print()




print("By Input")
brand = input("Enter a Mobile Brand Name = ")
model = input("Enter a Mobile Model = ")
price = int(input("Enter a Mobile Price = "))
print()

m2 = Mobile_store()
m2.set_brand(brand)
m2.set_model(model)
m2.set_price(price)
m2.check_affordability()
m2.display()








