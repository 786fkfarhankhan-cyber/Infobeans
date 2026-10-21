# Rearrange the array in alternating positive and negative items
# Given an unsorted array Arr of N positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
# Note: Array should start with positive number.


arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
pos = []                       
neg = []                      

for x in arr:
    if x >= 0:
        pos.append(x)
    else:
        neg.append(x)

result = []
p = 0                          
q = 0                          
turn = 0                       

while p < len(pos) and q < len(neg):   
    if turn == 0:
        result.append(pos[p])
        p += 1
        turn = 1               
    else:
        result.append(neg[q])
        q += 1
        turn = 0               
while p < len(pos):
    result.append(pos[p])
    p += 1
while q < len(neg):
    result.append(neg[q])
    q += 1

print(result)                  











