# 2. Write a Python program to create a class called "Dog" with a name and breed attribute. Create two instances of the "Dog" class, set their attributes using the constructor and modify the attributes using the setter methods and print the updated values.


class Dog:
    def __init__(self):
        self.__name = None
        self.__breed = None
    def set_name(self,name):
        self.__name = name
    def set_breed(self,breed):
        self.__breed = breed
    def details(self):
        print(f"dog name = {self.__name} ")
        print(f" Dog breed = {self.__breed}")
d1 = Dog()
d1.set_name("Par")
d1.set_breed("german")
d1.details()










