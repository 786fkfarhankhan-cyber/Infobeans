# 30.
# Suppose A, B, C are arrays of integers of size M, N, and M + N respectively. The numbers in array A appear in ascending order while the numbers in array B appear in descending order. Write a Python progtam to produce third array C by merging arrays A and B in ascending order.



A = [1, 4, 7, 10]        
B = [9, 6, 3, 2]            

C = []                      
i = 0                      
j = len(B) - 1            

while i < len(A) and j >= 0:      
    if A[i] <= B[j]:
        C.append(A[i])     
        i += 1              
    else:
        C.append(B[j])     
        j -= 1              


while i < len(A):
    C.append(A[i])
    i += 1

while j >= 0:
    C.append(B[j])
    j -= 1

print(C)                   







