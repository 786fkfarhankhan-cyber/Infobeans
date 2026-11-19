# 18. Write a Python program to create a class called "Restaurant" with attributes for menu items, prices, and ratings, and methods to add and remove items, and to calculate average rating.

class Restaurant:
    def __init__(self,items,prices,ratings):
        self.__items = items
        self.__prices = prices
        self.__ratings = ratings
    
    def add_items(self, add_item, price):
        self.__items.append(add_item)
        self.__prices.append(price)
    def remove_items(self, remove_item):
        if remove_item in self.__items:
            index = self.__items.index(remove_item)
            self.__items.pop(index)
            self.__prices.pop(index)
        else:
            print("Item not found")
    def average_rating(self):
        if len(self.__ratings) == 0:
            return "No ratings available"

        return sum(self.__ratings) / len(self.__ratings)
    
    def get_details(self):
        print("Restaurant Menu:")

        for i in range(len(self.__items)):
            print(f"Item: {self.__items[i]}")
            print(f"Price: ₹{self.__prices[i]}")

        print("Ratings:", self.__ratings)
        print("Average Rating:", self.average_rating())


r1 = Restaurant(
    ["Pizza", "Burger", "Pasta"],
    [250, 120, 180],
    [4, 5, 3, 5, 4]
)

r1.add_items("Sandwich", 100)
r1.remove_items("Burger")

r1.get_details()







