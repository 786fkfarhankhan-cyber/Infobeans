class A:
    def m1(self):
        print("A-M1")
    def m2(self):
        print("A-M2")

class B(A):
    def m1(self):
        print("B-M1")

a_obj = B()
a_obj.m1()
a_obj.m2()


# we override method when we not satisfy parent class implementation so we overridding concept
