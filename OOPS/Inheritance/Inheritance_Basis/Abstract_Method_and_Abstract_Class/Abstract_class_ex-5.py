from abc import ABC, abstractmethod
class Test(ABC):
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