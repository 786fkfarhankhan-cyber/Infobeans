# 1. Write a program to reverse a string without using slicing ([::-1]).

# sr = input("Enter a String = ")
# for i in sr[::-1]:
#     print(i,end="")


sr = input("Enter a String = ")

rev = "" 
for ch in sr:
    rev = ch+rev

print(rev)