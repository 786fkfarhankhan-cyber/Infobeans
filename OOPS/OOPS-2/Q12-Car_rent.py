class Car:
    def __init__(self,car_no,model,price_per_day):
        self.__car_no = car_no
        self.__model = model
        self.__price_per_day = price_per_day
        self.__is_availibility = True

    def rent_car(self):
        if self.__is_availibility: # yani h available
            self.__is_availibility = False # false kara taki na ho kyuki wo available h hum usse rent pe dege aur pese kamaege
            print("Car Rented")
        else: # h nhi available
            print(" Srry Bro Car not Available")

    def return_car(self):
        if not self.__is_availibility: # nhi h abhi hamere pass car
            self.__is_availibility = True # uska ulta kara True yani h 
            print("Car returned")
        else: 
            print("Car was not rented")

    def calculate_rent(self, days):
        if days > 0:
            return days * self.__price_per_day
        else:
            print("Invalid days")
            return 0
 
    def __str__(self):
        return f"Car Number: {self.__car_no} , Model: {self.__model} , Available: {self.__is_availibility} "
 
 
c1 = Car("MP04AB1234", "Swift", 1500)
c1.rent_car()
print("Rent for 3 days:", c1.calculate_rent(3))
c1.return_car()
c1.__str__()

