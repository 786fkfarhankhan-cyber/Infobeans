# 31.
# Suppose X. Y, Z are arrays of integers of size M, N, and M + N respectively. The numbers in array X and Y appear in descending order. Write a Python program to produce third array Z by merging arrays X and Y in descending order.

X = [10, 7, 4, 1]       
Y = [9, 8, 3, 2]        
Z = []                  
i = 0                   
j = 0                   

while i < len(X) and j < len(Y):    
    if X[i] >= Y[j]:
        Z.append(X[i])  
        i += 1
    else:
        Z.append(Y[j])  
        j += 1


while i < len(X):
    Z.append(X[i])
    i += 1
while j < len(Y):
    Z.append(Y[j])
    j += 1

print(Z)                


