from abc import ABC, abstractmethod
class Test(ABC):
    def __init__(self,age,name,course,year):
        self.__age = age
        self.__name=name
        self.__course = course
        self.__year = year

    @classmethod
    @abstractmethod
    def wish(cls):
        print("Good Morning")


    @staticmethod
    @abstractmethod
    def hi():
        print("Hii")


    def hello(self):
        print("Hello")


class Exam(Test):
    def __init__(self,id):
        super().__init__("age","name","course","year")
        
    @classmethod
    def wish(cls):
        super().wish()
        print("Good Evening")

    @staticmethod
    def hi():
        print("Hii, how are you?")




obj = Exam()
obj.wish()
obj.hi()
obj.hello()