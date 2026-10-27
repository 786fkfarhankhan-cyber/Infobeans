# 1. Write a program to reverse a string without using slicing ([::-1]).and use Function

def reverse():
    # sr = input("Enter a String = ")
    # for i in sr[::-1]:
    #     print(i,end="")
        


    sr = input("Enter a String = ")

    rev = "" 
    for ch in sr:
        rev = ch+rev

    return rev

d = reverse()
print(d)

