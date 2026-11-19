# 8. Write a python  program to create class called "TrafficLight" with attributes for color and duration, and methods to change the color and check for red or green.
class TrafficLight:
    def __init__(self,color,duration):
        self.__color = color
        self.__duration = duration
    def change_color(self):
        if (self.__color == "Red"):
            self.__color = "Green"
        else:
            self.__color = "Red" 
    def check_red(self):
        return self.__color=="Red"
    def check_green(self):
        return self.__color=="Green"
    def display(self):
        print(f"Color: {self.__color}\nDuration: {self.__duration}\nChange Color: {self.change_color()}\nRed: {self.check_red()}\nGreen: {self.check_green()}")

obj1 = TrafficLight("Red","30 sec")
obj1.display()
print()

print("\nAfter changing color:")
obj1.change_color()
obj1.display()