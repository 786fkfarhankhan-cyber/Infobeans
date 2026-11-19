from abc import ABC, abstractmethod
class Solo(ABC):
    @abstractmethod
    def wish(self):
        pass

    def say_hello(self):
        print("Hello Magrib")

class Group(Solo):
    def wish(self):
        print("Hell0 Everyone")

obj = Group()
obj.wish()
obj.say_hello()
