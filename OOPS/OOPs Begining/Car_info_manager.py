# Car Info Manager
# Create a class Car with fields: brand, model, and year.
# Use setters to assign values. Create a method to print full car info.


print("*"*11,"By Setter Method","*"*11)

class Car_info_manager:
    def __init__(self):
        self.__brand = None
        self.__model = None
        self.__year = None

    def set_brand(self,car_brand):
        self.__brand = car_brand
    def set_model(self,car_model):
            self.__model = car_model
    def set_year(self,car_year):
            self.__year = car_year

    def car_details(self):
        print(f"Car Brand Name = {self.__brand} \nCar Model = {self.__model} \nCar Year = {self.__year}")   


# car_1 = Car_info_manager("Lambogini","Huracan",2025)
# car_2 = Car_info_manager("BMW","M5 2series",2026)
# car_3 = Car_info_manager("Ferrari","SP40",2024)
car_1 = Car_info_manager()

car_1.set_brand("Lambogini")
car_1.set_model("Huracan")
car_1.set_year("2023")
car_1.car_details()
print()



print("By Input")
brand = input("Enter a Brand = ")
model = input("Enter a Model = ")
year = int(input("Enter a Year = "))
print()

car_2 = Car_info_manager()
car_2.set_brand(brand)
car_2.set_model(model)
car_2.set_year(year)
car_2.car_details()




