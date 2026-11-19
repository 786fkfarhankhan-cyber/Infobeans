class ECommerceProduct:
    def __init__(self, name, price, category):
        self.__name = name
        self.__price = price
        self.__category = category
 
    @staticmethod
    def apply_gst(price, rate):
        return price + (price * rate / 100)
 
    def apply_category_discount(self, price):
        if self.__category == "Electronics":
            return price - (price * 10 / 100)
        elif self.__category == "Clothing":
            return price - (price * 20 / 100)
        else:
            return price
 
    def display_final_price(self):
        price_with_gst = ECommerceProduct.apply_gst(self.__price, 18)
        final_price = self.apply_category_discount(price_with_gst)
        print("Product:", self.__name)
        print("Category:", self.__category)
        print("Final Price:", final_price)
 
 
p1 = ECommerceProduct("T-Shirt", 1000, "Clothing")
p1.display_final_price()
