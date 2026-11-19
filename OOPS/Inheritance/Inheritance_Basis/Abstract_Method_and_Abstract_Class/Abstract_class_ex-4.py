from abc import ABC, abstractmethod
class Usa(ABC):

    @classmethod
    @abstractmethod
    def greet(cls):
        print("Hello Everyone")

# obj = Usa()
# obj.greet()
# TypeError: Can't instantiate abstract class Usa without an implementation for abstract method 'greet'
# No Object for Abstract Method

Usa.greet() # but class ke naam se method ko call kar sakte h

