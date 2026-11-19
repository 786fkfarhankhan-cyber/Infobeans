class A:
    def __init__(self):
        print("A Constructor Call")

class B(A):
    def __init__(self):
        super().__init__()
        print("B Constructor Call")

class C(B):
    def __init__(self):
        super().__init__()
        print("C Constructor Call")


obj = A()
print()
obj = B()
print()
obj = C()