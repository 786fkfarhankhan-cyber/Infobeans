# Jab Child class se parent class ki mehod call krni h we use - SUPER METHOD ()

# Syntax - Super(Current Class , Self or Cls)    ````error if static method````
# Super(Current case B is our Class , Next class before B or Parent Class in MRO)

# MRO = Method Resolution Order --- it is used to solve Ambuity error 

# Ambuity error :-
# In Python inheritance, an ambiguity error refers to situations where it’s unclear which method or attribute should be called because multiple parent classes define the same name.
# This often happens in multiple inheritance — especially in the diamond problem — where a class inherits from two or more classes that share a common ancestor.


class A:
    def m1(self):
        print("A-M1")
    def m2(self):
        print("A-M2")

class B(A):
    def m1(self):
        super().m1() # pehle parent class 
        print("B-M1")


obj = B()
obj.m1()





