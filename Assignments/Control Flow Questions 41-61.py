# Q41 — Find LCM of a numbers
# a = int(input("Enter first number = "))
# b = int(input("Enter second number = "))
# if a > b:
#     greater = a
# else:
#     greater = b
# while True:
#     if greater % a == 0 and greater % b == 0:
#         print("LCM =", greater)
#         break
#     greater = greater + 1

# Q42 — Find HCF of a numbers
# a = int(input("Enter first number = "))
# b = int(input("Enter second number = "))
# if a < b:
#     smaller = a
# else:
#     smaller = b
# hcf = 1
# for i in range(1, smaller + 1):
#     if a % i == 0 and b % i == 0:
#         hcf = i
# print("HCF =", hcf)

# Q43 — Convert Binary to Decimal
# binary = int(input("Enter a binary number = "))
# decimal = 0
# power = 0
# while binary > 0:
#     digit = binary % 10
#     decimal = decimal + digit * (2 ** power)
#     binary = binary // 10
#     power = power + 1
# print("Decimal =", decimal)

# Q44 — Interchange first and last digit of a number
# num = int(input("Enter a number: "))
# temp = num
#
# last_digit = num % 10
#
# # first digit find karne ke liye
# length = 0
# while temp >= 10:
#     temp = temp // 10
# first_digit = temp
#
# print("First digit:", first_digit, "Last digit:", last_digit)

# Q45 — WAP a prog. to calculate sum of digit of integer
# num = int(input("Enter a Number = "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum = sum + digit
#     num = num // 10        # isse num chota hota hai

# print(sum)


# Q46 — WAP Sum of first and last digit of a number
# num = int(input("Enter a number = "))
# temp = num
# while temp >= 10:
#     temp = temp // 10
# first = temp
# last = num % 10
# print("Sum of first and last digit =", first + last)


# Q47 — Print tables of all numbers between two entered numbers
# first_no = int(input("Enter first number = "))
# second_no = int(input("Enter second number = "))
# for num in range(first_no, second_no + 1):
#     print("Table of", num)
#     for i in range(1, 11):
#         print(num, "x", i, "=", num * i)


# Q48 — Factors of all numbers between two entered numbers
# first_no = int(input("Enter first number = "))
# second_no = int(input("Enter second number = "))
# for num in range(first_no, second_no + 1):
#     print("Factors of", num, "are:")
#     for i in range(1, num + 1):
#         if num % i == 0:
#             print(i)


# Q49 — Perfect numbers between two entered numbers
# first_no = int(input("Enter first number = "))
# second_no = int(input("Enter second number = "))
# for num in range(first_no, second_no + 1):
#     sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum = sum + i
#     if sum == num and num != 0:
#         print(num, "is Perfect Number")

# Q50 — Palindrome numbers between two entered numbers
# first_no = int(input("Enter first number = "))
# second_no = int(input("Enter second number = "))
# for num in range(first_no, second_no + 1):
#     temp = num
#     reverse = 0
#     while temp > 0:
#         digit = temp % 10
#         reverse = reverse * 10 + digit
#         temp = temp // 10
#     if reverse == num:
#         print(num, "is Palindrome")

# Q51 — Reverse all numbers between two entered numbers
# first_no = int(input("Enter first number = "))
# second_no = int(input("Enter second number = "))
# for num in range(first_no, second_no + 1):
#     temp = num
#     reverse = 0
#     while temp > 0:
#         digit = temp % 10
#         reverse = reverse * 10 + digit
#         temp = temp // 10
#     print("Reverse of", num, "is", reverse)

# Q52 — Armstrong numbers between two entered numbers
# first_no = int(input("Enter first number = "))
# second_no = int(input("Enter second number = "))
# for num in range(first_no, second_no + 1):
#     temp = num
#     length = 0
#     while temp > 0:
#         length += 1
#         temp = temp // 10
#     temp = num
#     total = 0
#     while temp > 0:
#         digit = temp % 10
#         total = total + (digit ** length)
#         temp = temp // 10
#     if total == num:
#         print(num, "is Armstrong Number")

# Q53 — Strong numbers between two entered numbers
# first_no = int(input("Enter first number = "))
# second_no = int(input("Enter second number = "))
# for num in range(first_no, second_no + 1):
#     temp = num
#     total = 0
#     while temp > 0:
#         digit = temp % 10
#         fact = 1
#         i = 1
#         while i <= digit:
#             fact = fact * i
#             i = i + 1
#         total = total + fact
#         temp = temp // 10
#     if total == num:
#         print(num, "is Strong Number")

# Q54 — Even numbers between two entered numbers
# first_no = int(input("Enter first number = "))
# second_no = int(input("Enter second number = "))
# for num in range(first_no, second_no + 1):
#     if num % 2 == 0:
#         print(num)


# Q55 — Odd numbers between two entered numbers
# start = int(input("Enter start number = "))
# end = int(input("Enter end number = "))
# for num in range(start, end + 1):
#     if num % 2 != 0:
#         print(num)

# Q56 — Factorial of all numbers between two entered numbers
# st = int(input("Enter start number = "))
# d = int(input("Enter end number = "))
# for num in range(st, d + 1):
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     print("Factorial of", num, "is", fact)

# Q57 — Prime numbers between two entered numbers
# start = int(input("Enter start number = "))
# end = int(input("Enter end number = "))
# for num in range(start, end + 1):
#     if num < 2:
#         continue
#     prime = True
#     i = 2
#     while i <= num // 2:
#         if num % i == 0:
#             prime = False
#             break
#         i = i + 1
#     if prime:
#         print(num, "is Prime")


# Q58 — Convert Decimal to Binary (without array)
# num = int(input("Enter a decimal number = "))
# binary = 0
# place = 1
# while num > 0:
#     rem = num % 2
#     binary = binary + rem * place
#     place = place * 10
#     num = num // 2
# print("Binary =", binary)


# Q59 — WAP to find out Sum of integers between 100 and 200 divisible by 9
# total = 0
# for i in range(100, 201):
#     if i % 9 == 0:
#         total = total + i
# print("Sum =", total)

# Q60 — Square, Cube, Square Root of numbers from 1 to N
# n = int(input("Enter N = "))
# for i in range(1, n + 1):
#     square = i * i
#     cube = i * i * i
#     sqrt = i ** 0.5
#     print(i, " Square =", square, ", Cube =", cube, ", Square Root =", sqrt)


# Q61 — Leap years between two entered years
# start = int(input("Enter start year = "))
# end = int(input("Enter end year = "))
# for year in range(start, end + 1):
#     if year % 4 == 0 and year % 100 != 0:
#         print(year, "is Leap Year")
#     elif year % 400 == 0:
#         print(year, "is Leap Year")







