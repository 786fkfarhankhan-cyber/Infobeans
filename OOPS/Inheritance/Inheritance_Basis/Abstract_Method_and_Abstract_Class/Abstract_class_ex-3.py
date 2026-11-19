from abc import ABC,abstractmethod
class Rome(ABC):
    @abstractmethod
    def greet(self):
        print("Good Night")

    def hii(self):
        print("Hello")


class Italy(Rome):
    def greet(self):
        super().greet()
        print("You Know What You do")


obj = Italy()
obj.greet()
