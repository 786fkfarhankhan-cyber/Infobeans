# Q21 — Series: 1  4  9  16  25  …..
# n = int(input("Enter n terms: "))
# for i in range(0,n+1):
#     sq = i*i
#     print(sq)


# Q22 — Series: 1  8  27  64  125  …..
# n = int(input("Enter n terms: "))
# for i in range(1,n+1):
#     cube = i*i*i
#     print(cube)


# Q23 — Series: 1  9  25  49  81  …..
# n = int(input("Enter n terms: "))
# for i in range(1,n+1):
#     if i % 2 == 0:
#         continue
#     else:
#         sq = i*i
#         print(sq)



# Q24 — Series: 0  4  16  36  64  ….. 1 2 3 4 5 6 7 8
# n = int(input("Enter n terms: "))
# for i in range(1,n+1):
#     if i % 2 == 0:
#         sq = i*i
#         print(sq)
#
#     else:
#         continue


# Q25 — Series: 1  27  125  343  …………
# n = int(input("Enter n terms: "))
# for i in range(1,n+1):
#     if i % 2 == 0:
#         continue
#
#     else:
#         cube = i*i*i
#         print(cube)


# Q26 — Series: 0, 8, 64, 216 ... n terms
# n = int(input("Enter n terms: "))
# for i in range(0, n):
#     term = (2 * i) ** 3
#     print(term)


# Q27 — Pattern: * # * # * # ...
# n = int(input("Enter n terms: "))
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         print("*", end=" ")
#     else:
#         print("#", end=" ")


# Q28 — Series: 1 2 3 4 Hello 6 7 8 9 Hello 11 12 ...
# n = int(input("Enter n terms: "))
# for i in range(1, n + 1):
#     if i % 5 == 0:
#         print("Hello", end=" ")
#     else:
#         print(i, end=" ")


# Q29 — Series: 1, 11, 111, 1111, 11111 ... n terms
# n = int(input("Enter n terms: "))
# num = 0
# for i in range(1, n + 1):
#     num = num * 10 + 1
#     print(num)

# Q30 — Sum of 1+11+111+1111+11111 ... n terms
# terms = int(input("Enter a Number = "))
# term = 1
# sum = 0
# count = 1
# while count<= term:
#     sum = sum+term
#     term = term*10+1
#     count = count+1
# print("sum = ",sum)


# Q31 — Series: 9, 99, 999, 9999, 99999 ...
# n = int(input("Enter n terms: "))
# num = 0
# for i in range(1, n + 1):
#     num = num * 10 + 9
#     print(num,end= " ")


# Q32 — Pattern: A b C d E f G h ... n terms
# terms = int(input("Enter no. of terms: "))
#
# upper_Alp = 65
# lower_Alp = 97
# count = 1
#
# while count <= terms:
#     if count % 2 != 0:
#         print(chr(upper_Alp), end=" ")
#     else:
#         print(chr(lower_Alp), end=" ")
#
#     upper_Alp = upper_Alp + 1
#     lower_Alp = lower_Alp + 1
#     count = count + 1
# print()

# Q33 — Print alphabets in reverse order
# for i in range(90, 64, -1):
#     print(chr(i), end=" ")


# Q34 — WAP to check whether entered number is perfect or not
# num = int(input("Enter a Number = "))
# sum = 0
# #for i in range(1,num):
# for i in range(1,num//2+1):

#     if num % i == 0 :
#         sum = sum + i
# if sum == num:
#     print("It is Perfect Number")
# else:
#     print("It is not a Perfect Number")

# Q35 — WAP to count number of digits
# num = int(input("Enter a Number = "))
# print(num)
# count = 0
# while num > 0:
#     count += 1
#     num = num // 10
# print(count)


# Q36 — WAP to calculate reverse number
# num = int(input("Enter a number = "))
# reverse = 0
# while num>0:

#     n = num % 10
#     reverse = reverse * 10 + n
#     num = num//10
# print(reverse)

# Q37 — WAP to enter a num to check palindrome or not
# num = int(input("Enter a number = "))
# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10        # last digit nikala kyuki modulus reminder deta h
#     reverse = reverse * 10 + digit   # reverse mein joda
#     num = num // 10         # last digit hataya decimal ke baad wala floor division ka use kara h

# if reverse == original:
#     print("It is Palindrome")
# else:
#     print("It is not Palindrome")


# Q38 — WAP to check num Armstrong or not
# n = int(input("Enter a Number = "))
# length = 0
# temp = n
# while n != 0:
#     length += 1
#     n = n//10
# print(f"Length Of {temp} is {length}")


# sum  = 0
# n = temp
# while n != 0:
#     r = n % 10
#     sum = sum + (r ** length)
#     n = n // 10
# if sum == temp:
#     print("Armstrong")
# else:
#     print("Not Armstrong")


# Q39 — Check if a number is Strong Number
# num = int(input("Enter a number = "))
# temp = num
# total = 0
# while temp > 0:
#     digit = temp % 10
#     fact = 1
#     i = 1
#     while i <= digit:
#         fact = fact * i
#         i = i + 1
#     total = total + fact
#     temp = temp // 10
# if total == num:
#     print("Strong Number")
# else:
#     print("Not Strong Number")


# Q40 — Count even and odd digits
# num = int(input("Enter a Number = "))
# even_count = 0
# odd_count = 0
# while num > 0:
#     digit = num % 10
#     if digit % 2 == 0:
#         even_count = even_count + 1
#     else:
#         odd_count = odd_count + 1
#     num = num // 10
# print("Even digits count:", even_count)
# print("Odd digits count:", odd_count)
