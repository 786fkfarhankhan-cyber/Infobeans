# Polymorphism = one thing with different implementation , 
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def get_area(self):
        r = float(input("Enter Radius = "))
        print(f"Area Circle = {r*r*3.14}")

class Circle(Shape):
    def get_area(self):
        r = float(input("Enter Radius = "))
        print(f"Area Circle = {r*r*3.14}")


class Circle(Shape):
    def get_area(self):
        r = float(input("Enter Radius = "))
        print(f"Area Circle = {r*r*3.14}")