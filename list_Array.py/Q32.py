# 32.
# Given two arrays of integers A and B of sizes M and N respectively. Write a Write a Python program, which will produce a third array named C. such that the following sequence is followed.
# All even numbers of A from left to right are copied into C from left to right.
# All odd numbers of A from left to right are copied into C from right to left.
# All even numbers of B from left to right are copied into C from left to right.
# All old numbers of B from left to right are copied into C from right to left.
# e.g., A is {3, 2, 1, 7, 6, 3} and B is {9, 3, 5, 6, 2, 8, 10} the resultant array C is {2, 6, 6, 2, 8, 10, 5, 3, 9, 3, 7, 1, 3}


A = [3, 2, 1, 7, 6, 3]
B = [9, 3, 5, 6, 2, 8, 10]

C = [0] * (len(A) + len(B))   
front = 0                      
back = len(C) - 1              

for x in A:
    if x % 2 == 0:            
        C[front] = x
        front += 1            
    else:                      
        C[back] = x
        back -= 1             

for x in B:                    
    if x % 2 == 0:
        C[front] = x
        front += 1
    else:
        C[back] = x
        back -= 1

print(C)             




