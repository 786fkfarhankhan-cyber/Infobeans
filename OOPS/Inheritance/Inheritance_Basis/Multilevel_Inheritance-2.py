class A:
    pass
class B(A): # B - A - OBJ
    pass
class C(A): # C-A - OBJ
    pass
class D(C,B):   # D - C - B - A - OBJ
    pass

print(f"A MRO = {A.mro()}")
print(f"B MRO = {B.mro()}")
print(f"C MRO = {A.mro()}")
print(f"D MRO = {C.mro()}")


