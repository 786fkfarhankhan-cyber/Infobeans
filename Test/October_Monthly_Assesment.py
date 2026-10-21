# Q5. Dictionaries — Word Frequency (5 Marks)

# Write a program to count the frequency of each word in a sentence using a dictionary. Treat uppercase and lowercase words as the same.

# sentence = "Python is easy and Python is powerful"

# sen = "Python is easy and Python is powerful"
# word = list(sen.split(" "))
# dy = {}
# for ch in word:
#     if ch in dy:
#         dy[ch]+=1
#     else:
#         dy[ch]=1

# print(dy)




# Q4. Sets — Common and Unique Elements (5 Marks)

# Given two lists, find:
# Elements common to both lists.
# Elements that appear in either list but not in both.
# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 60, 70]
# Expected output:
# Common elements: {30, 40}
# Unique elements: {10, 20, 50, 60, 70}

# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 60, 70]
# w = set()
# s = set(list1)
# d = set(list2)

# for i in s:
#     if i not in d:
#         w.add(i)
# for i in d :
#     if i not in s:
#         w.add(i)
# print(f"This are Unique Elements = {w}")
# s.intersection_update(d) 
# print(f"This are common elements = {s}")



# Q1. If-Else — Number Classification (5 Marks)
# Write a program that accepts an integer and checks whether it is a Harshad number.
# A number is a Harshad number if it is divisible by the sum of its digits.
# Example:
# Input: 18
# Output: Harshad Number (18 is divisible by 1 + 8 = 9)

# num = int(input("Enter number = "))
# reserve = num  
# sum=0
# while num!=0:
#     rem = num%10
#     sum += rem
#     num//=10
# if reserve%sum==0:
#     print("It is a Harshad number")
# else:
#     print("It is not Harshad number")



# Q2. Loops — Prime Numbers (5 Marks)
# Write a program to print all prime numbers between 1 and 100. Do not use any built-in prime-checking function.
# Expected output: 2, 3, 5, 7, 11, ... 97

for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=", ")











