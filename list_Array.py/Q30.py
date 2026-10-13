# 30.
# Suppose A, B, C are arrays of integers of size M, N, and M + N respectively. The numbers in array A appear in ascending order while the numbers in array B appear in descending order. Write a Python progtam to produce third array C by merging arrays A and B in ascending order.



A = [1, 4, 7, 10]           # ascending
B = [9, 6, 3, 2]            # descending

C = []                      # merged answer
i = 0                       # A pe ungli, shuru se
j = len(B) - 1              # B pe ungli, PEECHE se (kyunki B ulta hai)

while i < len(A) and j >= 0:      # jab tak dono mein kuch bacha ho
    if A[i] <= B[j]:
        C.append(A[i])      # A wala chhota hai, C mein daalo
        i += 1              # A mein aage
    else:
        C.append(B[j])      # B wala chhota hai, C mein daalo
        j -= 1              # B mein peeche se aage (j ghatta hai)

# jo array bacha uska baki sab seedha jod do
while i < len(A):
    C.append(A[i])
    i += 1

while j >= 0:
    C.append(B[j])
    j -= 1

print(C)                    # [1, 2, 3, 4, 6, 7, 9, 10]







