# 1. Write a program to reverse a string without using slicing ([::-1]).

# sr = input("Enter a String = ")
# for i in sr[::-1]:
#     print(i,end="")


sr = input("Enter a String = ")

rev = "" # ye ek empty str banai h taki bad me isse use kare
for ch in sr:
    rev = ch + rev

print(rev)