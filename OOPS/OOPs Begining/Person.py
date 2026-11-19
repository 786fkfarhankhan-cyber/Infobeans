# 1. Write a Python program to create a class called "Person" with a name and age attribute. Create two instances of the "Person" class, set their attributes using the constructor, and print their name and age.

class Person:
    def __init__(self):
        self.__name = None
        self.__age  = None
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age
    def details(self):
        print(f"Your Name is , {self.__name}")
        print(f"Your Age is , {self.__age}")

p1 = Person()
p1.set_name("Farhan Khan")
p1.set_age(21)  
p1.details()
        


print("By Input")
name = input("Enter Ur Name : ")
age = int(input("Enter a Ur age : "))

p2 = Person()
p2.set_name(name)
p2.set_age(age)
p2.details()
















