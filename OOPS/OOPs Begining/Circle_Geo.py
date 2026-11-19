# Circle Geometry
# Create a class Circle with field radius.
# Use a setter to assign radius. Add methods to compute area and circumference.


class Circle:
    def __init__(self):
        self.__radius = None
    def set_radius(self,radius):
        self.__radius = radius
    def circle_area(self):
        pie = 22/7
        area = pie * (self.__radius*self.__radius)
        return area
    def circle_circumference(self):
        pie = 22/7
        circumference = pie*self.__radius*2
        return circumference

    def details(self):
        print(f"Radius of Circle : {self.__radius}")
        print(f"Area of Circle : {self.circle_area()}") # always write self then function name
        print(f"Area of Circle Circumference : {self.circle_circumference()}")

c1 = Circle()
c1.set_radius(3)
c1.circle_area()
c1.circle_circumference()
c1.details()























