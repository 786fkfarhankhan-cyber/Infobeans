class A:
    def wish(self):
        print("Good Morning")
class B:
    def wish(self):
        print("Good Evening")
class C(B,A): # C - B - A
    pass
obj = C()
obj.wish()

