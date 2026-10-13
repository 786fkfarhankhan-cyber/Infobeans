# 1) WAP to print a statement 1000 number of times.
# statement = " Helo guys " 
# for i in range(1,1001):
#     print(statement)

# 2) WAP to print N natural number
# n = int(input("Enter NUmber : ")) # Natural number lene h
# for i in range(1, n+1):
#     print(i)


#  3) WAP to find out the sum of N natural number.
# n = int(input("Enter Number: "))
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# print("Sum is", sum)

# Q4 — WAP to print table of a number
# num = int(input("Enter number: "))
# for i in range(1, 11):
#     print(num, "x", i, "=", num*i)


# Q5 — WAP to find out the factorial of a number.
# num = int(input("Enter number: "))
# fact = 1
# for i in range(1, num+1):
#     fact = fact * i
# print("Factorial is", fact)
#
# OR
#
# n = int(input("Enter a number = "))
# f = 1
# while n>1:
#     f=f*n
#     n-=1
# print(f)


# Q6 — WAP to find out the factors of a number.
# num = int(input("Enter number: "))  # A factor of a number is a number that divides the given number exactly, leaving no remainder.
# for i in range(1, num+1):
#     if num % i == 0:
#         print(i)


# Q7 — WAP to check whether entered number is prime or not.
# n =11
# i = 2
# while i<=n//2:
#     if n%i==0:
#         break
#     i+=1
# if i> n//2 and n>1:
#     print("prime")
# else:
#     print("Not Prime")

# Q8 — WAP to print Fibonacci series.
# n = int(input("How many terms: "))
# a = 0
# b = 1
#
# for i in range(n):
#     print(a)
#     c = a + b     # naya number calculate hoga
#     a = b         # a ko b hoga
#     b = c         # b ko c ki value milegi


# Q9 — WAP to print N even numbers.
# n = int(input("Enter N: "))
# for i in range(1, n+1):
#     if i % 2 == 0:
#         print(i)


# Q10 — WAP to print Even numbers upto N.
# n = int(input("Enter N: "))
# for i in range(2, n+1, 2):
#     print(i)


# Q11 — WAP to print N odd numbers.
# n = int(input("Enter N: "))
# for i in range(1, n+1):
#     if i % 2 != 0:
#         print(i)


# Q12 — WAP to print Odd numbers upto N.
# num = int(input("Enter a number = "))
# for i in range(1,num+1):
#     if i%2==0:
#         continue
#     else:
#         print(i)


# Q13 — WAP to print N natural numbers in reverse order
# n = int(input("Enter N: "))
# for i in range(n, 0, -1):
#     print(i)


# Q14 — WAP to print alphabets in uppercase
# char = input("Enter a Alphabet = ")
# for i in char:
#     print(i.upper())


# Q15 — WAP to print alphabets in lowercase
# char = input("Enter a Alphabet = ")
# for i in char:
#     print(i.lower(),end="")


# Q16 — Series: -6  -3  0  3  6  9  ……. n terms [where n is even]
# n = int(input("Enter n: "))
# if n % 3 ==0:
#     for i in range(-n,n+1,3):
#         print(i)


# Q17 — Series: 1  2  4  7  11  16  …… n terms
# n = int(input("Enter n: "))
# term = 1
# gap = 1
# for i in range(n):
#     print(term)          
#     term = term + gap    
#     gap = gap + 1         


# Q18 — Series: 1  2  2  4  8  32  …… n terms
# n = int(input("Enter n: "))
# a = 1
# b = 2
#
# for i in range(n):
#     print(a , end=" ")
#     c = a * b     # naya term = pichle do ka multiply
#     a = b         # a ko aage badhao
#     b = c         # b ko bhi aage badhao


# Q19 — 1 + 1/2 + 1/3 + 1/4 + 1/5 ….. n terms (find out sum)
# n = int(input("Enter n terms: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + 1/i
# print(f"Sum = {sum}")



# Q20 — Series: 0  7  14  21  28  35  …..
# n = int(input("Enter n terms: "))
# for i in range(0,n+1):
#     term = 7*i
#     print(term)