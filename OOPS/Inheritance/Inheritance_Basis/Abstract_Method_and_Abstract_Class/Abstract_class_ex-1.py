# from abc import ABC,abstractmethod
# # ABstract Class Ka object nhi banta
# class Test(ABC):
#     @abstractmethod
#     def wish(self):
#         pass

# obj = Test() 
# print(obj)



# from abc import ABC,abstractmethod
# ABstract Class method ko override nhi kiya 
# class Test(ABC):
#     @abstractmethod
#     def wish(self):
#         pass

# obj = Test() 
# print(obj)
# TypeError: Can't instantiate abstract class Test without an implementation for abstract method 'wish'




from abc import ABC , abstractmethod
class Test(ABC): # parent Class
    @abstractmethod
    def wish(self):
        pass

class Na(Test): # Child Class
    def wish(self):
        print("We Are come to Existance")
        print("Time will Come")

obj = Na()
obj.wish()























