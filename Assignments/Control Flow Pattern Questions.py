# Q62.******
# n = int(input("Enter n = "))
# for i in range(n):
#     print("*", end="")

# Q63
# n = int(input("Enter n = "))
# for i in range(n):
#     print("*")

# Q64 (Diagonal Star)

# for i in range (1,6):
# 	for  j in range (1,6):
# 		if i != j:
# 			print(" ", end = " ")
# 		else:
# 			print("*", end = " ")
# 	print()

# Q65 
# *****
# *****
# *****
# *****

# for i in range (1,6):
# 	for j in range (1,6):
# 		print("*", end = " ")
# 	print()

# Q66
# 12345
# 12345
# 12345
# 12345
# 12345

# for i in range (1,6):
# 	for j in range (1,6):
# 		print(j, end = " ")
# 	print()

# Q67
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 
# for i in range (1,6):
# 	for j in range (1,6):
# 		print(i, end = " ")
# 	print()


# Q68
# 1
# 00
# 111
# 0000
# 11111

# for i in range(1,6):
#     for j in range(i):
#         if i %2 !=0:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()


# Q69
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

# Q70
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# Q71
# 1
# 22
# 333
# 4444
# 55555

# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print()

# Q72
# A
# AB
# ABC
# ABCD
# ABCDE

# for i in range(1, 6):
#     for j in range(65, 65 + i):
#         print(chr(j), end="")
#     print()

# Q73
# a
# ab
# abc
# abcd
# abcde

# for i in range(1, 6):
#     for j in range(97, 97 + i):
#         print(chr(j), end="")
#     print()

# Q74
# 1
# 01
# 101
# 0101
# 10101

# n = int(input("Enter n = "))
# for i in range(1, n + 1):
#     for j in range(i):
#         if (i - 1 - j) % 2 == 0:
#             print(1, end="")
#         else:
#             print(0, end="")
#     print()



# Q75
# 1
# 23
# 456
# 78910

# num = 1
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(num, end="")
#         num = num + 1
#     print()

# Q76
# A
# BB
# CCC
# DDDD
# EEEEE

# asci_val = 65
# for i in range(1, 6):
#     for j in range(1, i+1): # yha i + 1 isliye likha h kyuki i = 1 to 1 se 1 tak jaega yani loop ko run karne ke liye i + 1 = 1+1 =2 to (1,2) to ek bar chalega
#         print(chr(asci_val), end="")
#     asci_val = asci_val + 1
#     print()


# Q77
# a
# bc
# def
# ghij
# klmno
# alp = 97
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(chr(alp), end="")
#         alp = alp + 1
#     print()

# Q78
# *
# ##
# ***
# ####
# *****

# for i in range(1,6):
#     for j in range(i):
#         if i % 2 != 0:
#             print("*",end="")
#         else:
#             print("#",end="")
#     print()

# Q79
# 1
# 10
# 101
# 1010
# 10101
# for i in range(1,6):
#     for j in range(i):
#         if j % 2 == 0:
#             print("1", end="")
#         else:
#             print("0", end="")
#     print()

# Q80
# *
# * *
# *  *
# *   *
# * * * * *
# for i in range(1, 6):
#     for j in range(1,i+1):
#         if j>2 and i>1 and  i<5:
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()

# Q81
# 1
# 12
# 1 3
# 1  4
# 12345

# for i in range(1, 6):
#     for j in range(1, i+1):
#         if i < 5 and j != 1 and j != i:
#             print(" ", end="")
#         else:
#             print(j, end="")
#     print()

# Q82
# 1
# 22
# 3 3
# 4  4
# 55555

# for i in range(1, 6):
#     for j in range(1,i+1):
#         if i < 5 and j != 1 and j != i:
#             print(" ",end="")
#         else:
#             print(i,end="")
#     print()


# Q83
# A
# AB
# A C
# A  D
# ABCDE
# for i in range(1,6):
#     for j in range(65,65+i):  # j = position hi rahega (1,2,3...)
#         if i==3 and j==66 or i==4 and (j==66 or j==67) :
#             print("_",end="")
#         else:
#             print(chr(j),end="")   # 64+1=65='A', 64+2=66='B'...
#     print()

# Q84
# a
# bc
# d f
# g  j
# klmno
# alp = 97
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if (i==3 and j==2) or (i==4 and (j==2 or j==3)):
#             print("_",end="")
#         else:
#             print(chr(alp), end="")
#         alp = alp + 1
#     print()

# Q85
# *
# **
# *@*
# *@@*
# * * * * *
# for i in range(1,6):
#     for j in range(1,i+1):
#         if i>j and j!=1 and i!=5:
#             print("@",end="")
#         else:
#             print("*",end="")
#     print()

# Q86
# 5
# 54
# 543
# 5432
# 54321
# for i in range(5,0,-1):

#     for j in range(5,i-1,-1):
#         print(j,end="")
   
    
#     print()

# Q87
# *
# *#
# *#*
# *#*#
# *#*#*
# for i in range(1,6):
#     for j in range(1,i+1):
#         if j % 2 == 0:
#             print("#",end="")
#         else:
#             print("*",end="")
#     print()


# Q88
# 1
# 10
# 1 1
# 1  0
# 10101
# for i in range(1, 6):
#     for j in range(1, i+1):
#         if i==3 and j==2 or i==4 and (j==2 or j==3):
#             print(" ",end="")
#         elif j%2==0:
#             print("0",end="")
#         else:

#             print("1",end="")
#     print()   

# Q89
# 1
# 123
# 12345
# 1234567
# 123456789
# for i in range(1,6):
#     for j in range(1,2*i):
#         print(j,end="")
#     print()

# Q90
# 1
# 222
# 33333
# 4444444
# 555555555
# for i in range(1,6):
#     for j in range(2*i-1):
#         print(i,end="")
#     print()

# Q91
# ***** 
# **** 
# ***
# **
# * 
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# Q92
# 12345
# 1234
# 123
# 12
# 1
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# Q93
# 55555
# 4444
# 333
# 22
# 1
# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end="")
#     print()

# Q94
# ABCDE
# ABCD
# ABC
# AB
# A
# for i in range(5,0,-1):
#     for j in range(65, 65 + i):
#         print(chr(j), end="")
#     print()

# Q95
# EEEEE
# DDDD
# CCC
# BB
# A

# asci_val = 69
# for i in range(5,0,-1):
#     for j in range(1, i+1): # yha i + 1 isliye likha h kyuki i = 1 to 1 se 1 tak jaega yani loop ko run karne ke liye i + 1 = 1+1 =2 to (1,2) to ek bar chalega
#         print(chr(asci_val), end="")
#     asci_val = asci_val - 1
    
#     print()

# Q96
# *****
# *  *
# * *
# **
# *

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         if j>2 and i>1 and  i<5:
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()

# Q97
# ABCDE
# A  D
# A C
# AB
# A
# for i in range(1,6):
#     for k in range(5,i):
#         print(" ",end="")
#     for j in range(6,i,-1):  # j = position hi rahega (1,2,3...)
#         if i==2 and (j==4 or j==5) or i==3 and j==5 :
#             print("_",end="")
#         else:
#             print(chr(71-j),end="")   # 64+1=65='A', 64+2=66='B'...
#     print()

# Q98
# *****
# ####
# ***
# ##
# *
# for i in range(5,0,-1):
#     for j in range(i):
#         if i % 2 != 0:
#             print("*",end="")
#         else:
#             print("#",end="")
#     print()

# Q99
# 55555
# 4  4
# 3 3
# 22
# 1
# for i in range(5,0,-1):
#     for space in range(5,0,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         if i==4 and (j==2 or j==3) or i==3 and j==2 :
#             print("_",end="")
#         else:
#             print(i,end="")
    
        
#     print()

# Q100
# 123456
# 54321
# 1234
# 321
# 12
# 1
# for i in range(1,7):
#     print(i,end="")
# print()

# for j in range(5,0,-1):
#     print(j,end="")
# print()

# for k in range(1,5):
#     print(k,end="")
# print()

# for t in range(3,0,-1):
#     print(t,end="")
# print()

# for b in range(1,3):
#     print(b,end="")
# print()

# for c in range(1,2):
#     print(c)



# Q101
# *
# **
# ****
# *******
# ***********
# for i in range(1,6):
#     for j in range(2*i+0):
#         print("*",end="")
#     print()


# Q102
# A
# BCD
# EFGHI
# JKLMNOP
# alp = 65
# for i in range(1, 6):
#     for j in range(1, i *2):
#         print(chr(alp), end="")
#         alp = alp + 1
#     print()


# Q103
# 54321
# 5432
# 543
# 54
# 5
# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end="")
#     print()

# Q104
# 1
# 12
# 123
# 1234
# 12345
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# Q105
# 1
# 22
# 333
# 4444
# 55555
# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print()

# Q106
# 5
# 44
# 333
# 2222
# 11111
for i in range(5,0,-1):
    for j in range(6,i,-1):
        print(i,end="") 
    print()

# Q107
# A
# AB
# ABC
# ABCD
# ABCDE
# for i in range(1, 6):
#     for j in range(65, 65 + i):
#         print(chr(j), end="")
#     print()

# Q108
# 1
# 11
# 1*1
# 1**1
# 11111
for i in range(1, 6):
    for j in range(1, i+1):
        if (i==3 and j==2 or i==4 and (j==3 or j==2)):
            print("*",end="")
        else:

            print("1",end="")
    print()   

# Q109
# A
# AB
# A_C
# A__D
# ABCDE
# for i in range(1,6):
#     for k in range(i,5):
#         print(" ",end="")
#     for j in range(1, i+1):  # j = position hi rahega (1,2,3...)
#         if i==3 and j==2 or i==4 and (j==2 or j==3):
#             print("_",end="")
#         else:
#             print(chr(64+j),end="")   # 64+1=65='A', 64+2=66='B'...
#     print()


# Q110
# 1
# 10
# 101
# 1010
# 10101
# for i in range(1, 6):
#     for space in range(5,i,-1):
#         print(" ",end="")
#     for j in range(1, i+1):
#         if j%2==0:
#             print("0",end="")
#         else:

#             print("1",end="")
#     print() 


# Q111
# 12345
#  1234
#   123
#    12
#     1
# for i in range(5,0,-1):
#     for _ in range(5,i,-1):
#             print(" ",end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     # for _ in range(5,i,-1):
#     #     print(" ",end="")
    
#     print()


# Q112
# 55555
#  4444
#   333
#    22
#     1
# for i in range(5,0,-1):
#     for _ in range(5,i,-1):
#         print(" ",end="")
#     for j in range(i):
#         if i==2 and j==3 or j==5:
#             print("_",end="")
#         else:
#             print(i,end="")
#     print()


# Q113
# 12345
#  1__4
#   1_3
#    12
#     1
# for i in range(5,0,-1):
#     for k in range(i,5):
#         print(" ",end="")
#     for j in range(1,i+1):
#         if(i==4 and(j==2 or j==3)) or ( i==3 and j==2):
#             print("_",end="")
#         else:
#             print(j,end="")
#     print()


# Q114
# 55555
#  4__4
#   3_3
#    22
#     1
# for i in range(5,0,-1):
#     for k in range(i,5):
#         print(" ",end="")
#     for j in range(1,i+1):
#         if(i==4 and(j==2 or j==3)) or ( i==3 and j==2):
#             print("_",end="")
#         else:
#             print(i,end="")
#     print()


# Q115
# ABCDE
#  A__D
#   A_C
#    AB
#     A

# for i in range(5,0,-1):
#     for k in range(i,5):
#         print(" ",end="")
#     for j in range(1, i+1):           # j = position hi rahega (1,2,3...)
#         if (i==4 and (j==2 or j==3)) or (i==3 and j==2):
#             print("_",end="")
#         else:
#             print(chr(64+j),end="")   # 64+1=65='A', 64+2=66='B'...
#     print()


# Q116
# ABCDE
#  ABCD
#   ABC
#    AB
#     A
# for i in range(5,0,-1):
#     for k in range(i,5):
#         print(" ",end="")
#     for j in range(1, i+1):           # j = position hi rahega (1,2,3...)
#         print(chr(64+j),end="")   # 64+1=65='A', 64+2=66='B'...
#     print()


# Q117
# 11111
#  2222
#   333
#    44
#     5
# for i in range(1,6):
#     for space in range(1,i):
#         print(" ",end="")
#     for j in range(6,i,-1):
#         print(i,end="")
#     print()


# Q118
#     * 
#    * * 
#   * * * 
#  * * * * 
# for i in range(1,6):
#     for space in range(5,i,-1):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end=" ")
#     print()


# Q119
#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5 
# for i in range(1,6):
#     for k in range(5,i,-1):
#         print(" ",end="")
#     for j in range(1, i+1):  
#         print(j,end=" ")   
#     print()


# Q120
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
# for i in range(1,6):
#     for k in range(5,i,-1):
#         print(" ",end="")
#     for j in range(1, i+1):  # j = position hi rahega (1,2,3...)
#         print(chr(64+j),end=" ")   # 64+1=65='A', 64+2=66='B'...
#     print()



# Q121
#     X 
#    X X 
#   X _ X 
#  X _ _ X 
# X X X X X 

# for i in range(1,6):
#     for space in range(5,i,-1):
#         print(" ",end="")
#     for j in range(i):
#         if i==3 and j==1 or i==4 and (j==2 or j==1):
#             print("_",end=" ")
#         else:
#             print("X",end=" ")
#     print()



# Q122
#     *
#    ***
#   *****
#  *******
# *********

# for i in range(1,6):
#     for space in range(5,i,-1):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# Q123
#     1
#    123
#   12345
#  1234567
# 123456789

# for i in range(1,6):
#     for space in range(5,i,-1):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print(j+1,end="")
#     print()


# Q124
#     A
#    ABC
#   ABCDE
#  ABCDEFG
# ABCDEFGHI

# for i in range(1,6):
#     for space in range(5,i,-1):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print(chr(65+j),end="")
#     print()


# Q125
#         * 
#       * _ * 
#     * _ _ _ * 
#   * _ _ _ _ _ * 
# * * * * * * * * * 

# for i in range(1,6):
#     for k in range(5,i,-1):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         if (i==2 and j==1) or ( i==3 and (j==1 or j==2 or j==3 )) or (i==4 and (j==1 or j==2 or j==3 or j==4 or j==5  )):
#             print("_",end=" ")
#         else:
#             print("*",end=" ")
#     print()



# Q126
#       1 
#      1 1 
#     1 2 1 
#    1 3 3 1 
#   1 4 6 4 1 
# n = int(input("Enter n = "))
# for i in range(n):
#     val = 1
#     print(" " * (n - i - 1), end="")
#     for j in range(i + 1):
#         print(val, end=" ")
#         val = val * (i - j) // (j + 1)
#     print()


# Q127
#         1 
#       1 * 1 
#     1 * * * 1 
#   1 * * * * * 1 
# 1 1 1 1 1 1 1 1 1 

# for i in range(1,6):
#     for k in range(5,i,-1):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         if (i==2 and j==1) or ( i==3 and (j==1 or j==2 or j==3 )) or (i==4 and (j==1 or j==2 or j==3 or j==4 or j==5  )):
#             print("*",end=" ")
#         else:
#             print("1",end=" ")
#     print()


# Q128
#     A
#    B B
#   C   C
#  D     D
# EEEEEEEEE

# for i in range(1,6):
#     for space in range(5,i,-1):
#         print(" ",end="")
#     for j in range(2*i-1):
#         if (i==2 and j==1) or (i==3 and ( j==1 or j==2 or j==3 )) or (i==4 and (j==1 or j==2 or j==3 or j==4 or j==5))  :
#             print("",end=" ")
#         else:
#             print(chr(i+64),end="")
#     print()


#Q129
#     #
#    *#* 
#   **#** 
#  ***#*** 
# ****#****

# Q130
# *********
#  *******
#   *****
#    ***
#     *

# for i in range(5,0,-1):
#     for space in range(5,i,-1):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()


# Q131
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

# for i in range(5,0,-1):
#     for _ in range(5,i,-1):
#         print("",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()


# Q132
# 123456789
#  1234567
#   12345
#    123
#     1
# for i in range(5,0,-1):
#     for _ in range(5,i,-1):
#         print("",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()


# Q133
# A B C D E 
#  A B C D 
#   A B C 
#    A B 
#     A 

# for i in range(5,0,-1):
#     for k in range(5,i,-1):
#         print(" ",end="")
#     for j in range(1, i+1):  # j = position hi rahega (1,2,3...)
#         print(chr(64+j),end=" ")   # 64+1=65='A', 64+2=66='B'...
#     print()


# Q134
# 5 5 5 5 5 
#  4 4 4 4 
#   3 3 3 
#    2 2 
#     1 

# for i in range(5,0,-1):
#     for k in range(5,i,-1):
#         print(" ",end="")
#     for j in range(i):
#         print(i,end=" ")
#     print()

# Q135
# 123456789
#  17
#   15
#    13
#     1

# for i in range(5,0,-1):
#     for space in range(5,i,-1):
#         print(" ",end="")
#     for j in range(2*i-1):
#         if (i==2 and j==1) or (i==3 and ( j==1 or j==2 or j==3 )) or (i==4 and (j==1 or j==2 or j==3 or j==4 or j==5))  :
#             print("",end="")
#         else:
#             print(j+1,end="")
#     print()



# Q136
# 123456789
#  1+++++7
#   1+++5
#    1+3
#     1

# for i in range(5,0,-1):
#     for space in range(5,i,-1):
#         print(" ",end="")
#     for j in range(2*i-1):
#         if (i==2 and j==1) or (i==3 and ( j==1 or j==2 or j==3 )) or (i==4 and (j==1 or j==2 or j==3 or j==4 or j==5))  :
#             print("+",end="")
#         else:
#             print(j+1,end="")
#     print()


# Q137
# x
# xx
# xxx
# xxxx
# xxxxx
# xxxx
# xxx
# xx
# x

# n = int(input("Enter n = "))
# for i in range(1, n + 1):
#     print("x" * i)
# for i in range(n - 1, 0, -1):
#     print("x" * i)


# Q138
# 1
# 12
# 123
# 1234
# 123
# 12
# 1

# n = int(input("Enter n = "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()


# Q139
# 1
# 12
# 123
# 1234
# 123
# 12
# 1

# for i in range(1,5):
#   k=1
#   for j in range(4,0,-1):
#     if i<j:
#       print(" ",end=" ")
#     else:
#       print(k,end=" ")
#       k+=1
#   print()    
 
# for i in range(1,4):
#   k=1
#   for j in range(1,5):
#     if i>=j :
#       print(" ",end=" ")
#     else:
#       print(k,end=" ")
#       k+=1
#   print()             

# Q140
# 1
# 1 2
# 1  3
# 1   4
# 1  3
# 1 2
# 1
# for i in range(1,5):
#   for j in range(1,5):
#     if j > i:
#       break
#     if j==1 or j==i:
#       print(j if j==1 else i, end=" ")
#     else:
#       print(" ", end="")
#   print()

# for i in range(3, 0, -1):
#   for j in range(1,5):
#     if j > i:
#       break
#     if j==1 or j==i:
#       print(j if j==1 else i, end=" ")
#     else:
#       print(" ", end="")
#   print()

#Q141
#    *
#   *_*
#  *_*_*
# *_*_*_*
#  *_*_*
#   *_*
#    *  

# for i in range(1,5):
#     for space in range(4,i,-1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         if j%2==1:
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# for i in range(3,0,-1):
#     for space in range(4,i,-1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         if j%2==1:
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# Q142
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *


# for i in range(1,6):
#     for space in range(5,i,-1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()
    
# for i in range(4,0,-1):
#     for space in range(5,i,-1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()


# Q143
#    *
#   *_* 
#  *___* 
# *_____*
#  *___* 
#   *_*
#    *
# for i in range(1,5):
#     for space in range(4,i,-1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()

# for i in range(3,0,-1):
#     for space in range(4,i,-1):
#         print(" ",end="")
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#             print("*",end="")
#         else:
#             print("_",end="")
#     print()


# Q144
# n = 7

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i==1 or i==n or j==1 or j==n or i==j or i+j==n+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# Q145
#     1
#    212
#   32123
#  4321234
# 543212345
# for i in range(1,6):
#     for space in range(5,i,-1):
#             print(" ",end="")
#     for j in range(i,1,-1):
#         print(j,end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# Q146
# *     *
# **    **
# ***   ***
# ****  ****
# *****  *****

# for i in range(1,6):
#   print("*"*i," " * (4-i),"*"*i  )

# Q147
# *****  *****
# ****  ****
# ***   ***
# **    **
# *     *
# for i in range(5,0,-1):
#   print("*"*i," " * (4-i),"*"*i  )


# Q148
# *****  *****
# ****   ****
# ***    ***
# **     **
# *      *
# *      *
# **     **
# ***    ***
# ****   ****
# *****  *****

# for i in range(5,0,-1):
#   print("*"*i, (" "*(5-i)),"*"*i)

# for i in range(1,6):
#   print("*"*i," " * (5-i),"*"*i  )    


# Q149
#         1         
#         2         
#         3         
#         4         
# 1 2 3 4 5 4 3 2 1 
#         4         
#         3         
#         2         
#         1         

# for i in range(1,10):
#     for j in range(1,10):
#         if i == 5 and j<=5:
#             print(j,end=" ")
#         elif j ==5 and i<5: 
#             print(i,end=" ")
#         elif i == 5 and j>5: 
#             print(10-j,end=" ")
#         elif j ==5 and i>5:
#             print(10-i,end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# Q150
#         1 
#       1 0 1 
#     1 0 1 0 1 
#   1 0 1 0 1 0 1 
# 1 0 1 0 1 0 1 0 1 


# for i in range(1, 6):
#     for space in range(5,i,-1):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         if j%2==0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()   


# Q151 WAP to print all the alphabets in pattern according to the selected case using switch case.
# choice = input("Enter U for Uppercase or L for Lowercase = ")
# if choice == 'U' or choice == 'u':
#     for i in range(65, 91):
#         print(chr(i), end=" ")
# elif choice == 'L' or choice == 'l':
#     for i in range(97, 123):
#         print(chr(i), end=" ")
# else:
#     print("Invalid choice")

#  WAP to calculate X to the power Y
# x = int(input("Enter a Number = "))
# y = int(input("Enter power = "))

# z = x**y
# print(z)