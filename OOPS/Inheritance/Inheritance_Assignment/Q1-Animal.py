# 1. Animal Sound System

# Create parent class Animal and child classes:

# Dog
# Cat
# Cow
# Override sound() method.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Barking")
class Cat(Animal):
    def sound(self):
        print("Mewww...")
class Cow(Animal):
    def sound(self):
        print("Muuu")
        
doco = Dog()
doco.sound()

jubi = Cat()
jubi.sound()

mi = Cow()
mi.sound()