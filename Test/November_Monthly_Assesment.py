# Q1. Longest Substring Without Repeating Characters

# Write a Python program to find the length of the longest substring that contains no repeating characters.
# Example:
# Input: abcabcbb
# Output: 3
# Explanation: "abc" is the longest substring.
# s = "abcabcbb"


# s = "abcdabcdbb"
# left  = 0
# right = 0
# ans = set()
# maxx = 0
# for right in range(len(s)):
#     ch = s[right]
#     while ch in ans:
#         ans.remove(s[left])
#         left+=1
#     ans.add(ch)       
#     maxx = max(maxx,right-left+1) 
# print(f"The longest substring without repeating characters : {maxx}")



# Q2. String Anagram

# Write a program to check whether two given strings are anagrams of each other.

# Anagrams contain the same characters with the same frequency, but in a different order.
# Input:
# String 1: listen
# String 2: silent

# Output: Anagram

# s1 = "listen"
# s2 = "silent"
# s1 = input("Enter a String = ")
# s2 = input("Enter a String = ")
# st1 = sorted(s1)
# st2 = sorted(s2)
# if st1 == st2:
#     print("Anagrams String")
# else:
#     print("Not Anagram")



# Q3. Longest Palindromic Substring

# Write a program to find the longest palindromic substring in a given string.
# Input: babad
# Output: bab
# Note: aba is also a valid answer.
# s = "babad"
# # t = "bab"
# t = input("Enter a substring which you want to find = ")
# if t in s:
#     if t == t[::-1] :
#         print("palindrome ")
#     else:
#         print(" not palindrome ")
# else :
#     print("T is not present in s")




# Q4. String Compression
# Write a program to compress a string by replacing consecutive repeated characters with the character followed by its frequency.
# Input: aaabbccccdaa

# s = "aaaabbbccd"
# count = 0
# word = ""
# ans = ""
# for ch in s:
#     if ch in word:
#         count+=1
#     else:
#         if word!="":
#             ans+=word+str(count)
#         word = ch
#         count = 1
# ans+=word+str(count)        
# print(ans)       



# Q5. OOP Programming Question: Product Management System
# Intermediate Level
#  10 Marks
# Problem Statement:

# Develop a Product Management System using Python OOP concepts.

# Create a class named Product with the following attributes:
# - product_id
# - product_name
# - category
# - price
# Requirements
# 1. Create a Product class with an appropriate constructor.
# 2. Create at least 5 product objects with different prices.
# 3. Store all product objects inside a list.
# 4. Implement a method display_product() to display product details.
# 5. Find and display the product having the second-highest price.
# 6. Display all products whose price is greater than ₹10,000.
# 7. Calculate and display the average price of all products.
# 8. Product must be unique on the basis of id

# class Product : 
#     def __init__(self,product_id , product_name,category,price):
#         self.__product_id = product_id
#         self.__product_name = product_name
#         self.__category = category
#         self.__price = price
#     def find(self):
#         if self.__price > 10000:
            
#             print(f"Product Name  = {self.__product_name}")
#             print(f"Product Category = {self.__category}")
#             print(f"Product Price = {self.__price}")
#         else:
#             pass
#     def avg_price(self,avg):
#         total = obj1.self.__price() + obj2.self.__price() + 
    
#     def product_details(self):
#         print(f"Product Id = {self.__product_id} \nProduct Name = {self.__product_name} \nProduct Category = {self.__category} \nProduct Price = {self.__price}")   

# l = []
# obj1 = Product()
# obj2 = Product()
# obj3 = Product()
# obj4 = Product()
# obj5 = Product()