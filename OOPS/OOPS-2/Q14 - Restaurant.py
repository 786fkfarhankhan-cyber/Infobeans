class RestaurantOrder:
    def __init__(self, table_no):
        self.__table_no = table_no
        self.__items = []
 
    def add_item(self, name, price):
        if price > 0:
            self.__items.append([name, price])
            print("Item added")
        else:
            print("Invalid price")
 
    def remove_item(self, name):
        for item in self.__items:
            if item[0] == name:
                self.__items.remove(item)
                print("Item removed")
                return
        print("Item not found")
 
    def calculate_total(self):
        total = 0
        for item in self.__items:
            total += item[1]
        return total
 
    @staticmethod
    def add_service_tax(total, rate):
        return total + (total * rate / 100)
 
    def __str__(self):
        total = self.calculate_total()
        final_bill = RestaurantOrder.add_service_tax(total, 5)

        return f"Table Number: {self.__table_no} ,\nItems: {self.__items},\nTotal: {total},\nBill with service tax: {final_bill}"
 
 
order1 = RestaurantOrder(5)
order1.add_item("Pizza", 250)
order1.add_item("Cold Drink", 50)
print(order1)
