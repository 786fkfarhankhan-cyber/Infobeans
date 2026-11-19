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


class Product:
    def _init_(self,iden,name,cate,price):
        self.__product_id = iden
        self.__product_name = name 
        self.__category = cate
        self.__price = price

    def display_product(self):
        print(f"Product ID:{self.__product_id}")
        print(f"Product Name:{self.__product_name}")
        print(f"Category:{self.__category}")
        print(f"Price:{self.__price} (Indian Rupees)")
        print("="*30)


    def _hash_(self):
        return hash(self.__product_id)

    def _eq_(self, obj):
        return self.__product_id == obj.iden

    def _str_(self):
        return f"Id: {self._product_id}\nName: {self.product_name}\nPrice: {self._price}"
    
    def get_price(self):
        return self.__price



class ProductManagement():
    __product_collection = {}
    def _init_(self, iden,name,cate,price):
        if iden in ProductManagement.__product_collection:
            print("="*30)
            print(f"{iden} Id already Present")
            print("="*30)
            return 
        ProductManagement.__product_collection[iden] = Product(iden, name, cate, price)


obj1 = ProductManagement(101,"Acer","Electronics(Laptop)",70000)
obj2 = ProductManagement(102,"Redmi","Electronics(Mobile Phone)", 15000)
obj3 = ProductManagement(103,"RD NoteBook","Education(NoteBook)",50)
obj4 = ProductManagement(104,"Pexpo","Water Bottel",150)
obj5 = ProductManagement(105,"Alto 800","Vehical(4 wheeler)",500000)



print("-"*10,"Product Management System","-"*10)
obj1.display_product()

print("*"*50)
