# 31.
# Suppose X. Y, Z are arrays of integers of size M, N, and M + N respectively. The numbers in array X and Y appear in descending order. Write a Python program to produce third array Z by merging arrays X and Y in descending order.

X = [10, 7, 4, 1]       # descending
Y = [9, 8, 3, 2]        # descending
Z = []                  # merged answer
i = 0                   # X pe ungli
j = 0                   # Y pe ungli

while i < len(X) and j < len(Y):    # dono mein kuch bacha ho
    if X[i] >= Y[j]:
        Z.append(X[i])  # X wala bada hai, Z mein daalo
        i += 1
    else:
        Z.append(Y[j])  # Y wala bada hai
        j += 1

# jo bacha usko seedha jod do
while i < len(X):
    Z.append(X[i])
    i += 1
while j < len(Y):
    Z.append(Y[j])
    j += 1

print(Z)                


