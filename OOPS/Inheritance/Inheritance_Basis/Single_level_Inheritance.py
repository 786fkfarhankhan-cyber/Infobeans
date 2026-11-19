class First:
    def call_rec(self):
        print("Call Receive")
    def call_rej(self):
        print("Call Reject")


class Second(First):
    def camera(self):
        print("Camera On")


# Parent Class
print("Parent Class Call")
obj1 = First()
First.call_rec(obj1)
First.call_rej(obj1)

print()


print("Second Class Call")
obj2 = Second()
Second.call_rec(obj2)
Second.call_rej(obj2)
Second.camera(obj2)

