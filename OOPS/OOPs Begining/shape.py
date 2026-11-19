# 16. Write a Python program to create a class called "Shape" with abstract methods for calculating area and perimeter, and subclasses for "Rectangle", "Circle", and "Triangle".



class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass



class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        pie = 22 / 7
        return pie * self.__radius * self.__radius

    def perimeter(self):
        pie = 22 / 7
        return 2 * pie * self.__radius

    def details(self):
        print("Shape: Circle")
        print(f"Radius: {self.__radius}")
        print(f"Area: {self.area():.2f}")
        print(f"Circumference: {self.perimeter():.2f}")



class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

    def perimeter(self):
        return 2 * (self.__length + self.__breadth)

    def details(self):
        print("Shape: Rectangle")
        print(f"Length: {self.__length}")
        print(f"Breadth: {self.__breadth}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")



class Triangle(Shape):

    def __init__(self, base, height, side1, side2, side3):
        self.__base = base
        self.__height = height
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def area(self):
        return 0.5 * self.__base * self.__height

    def perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def details(self):
        print("Shape: Triangle")
        print(f"Base: {self.__base}")
        print(f"Height: {self.__height}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")



c1 = Circle(7)
r1 = Rectangle(10, 5)
t1 = Triangle(10, 6, 10, 8, 6)



print("===== CIRCLE =====")
c1.details()

print("\n===== RECTANGLE =====")
r1.details()

print("\n===== TRIANGLE =====")
t1.details()






