# Rectangle Area Calculator
# Create a class Rectangle with fields: length, width.
# Use setters to assign values. Add a method to calculate area.



class Rectangle_area:
    def __init__(self):
        self.__length = None
        self.__breath = None

    def set_length(self,length):
        self.__length = length
    def set_breath(self,breath):
        self.__breath = breath
    def area(self):
        area = self.__length * self.__breath
        return area
    def details(self):
        print(f"Length of Rectangle : {self.__length}")
        print(f"Breath of Rectangle : {self.__breath}")
        print(f"Area of Rectangle : {self.area()}") # always write self then function name

r1 = Rectangle_area()
r1.set_length(6)
r1.set_breath(2)
r1.area()
r1.details()





