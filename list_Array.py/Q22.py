# Q.22 Max Sum in configuration
# Given an array(0-based indexing), you have to find the max sum of i*A[i] where A[i] is the element at index i in the array.The only operation allowed is to rotate(clock-wise or counter clock-wise) the array any number of times.

arr = [8, 3, 1, 2]
n = len(arr)

# pehle original array ka sum nikalo (ye pehla record)
best = 0
for i in range(n):
    best += i * arr[i]

# n baar rotate karo, har baar sum nikalo
for r in range(n):
    # ek step rotate (aakhri element ko aage laao)
    item = arr[-1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = item

    # is rotation ka sum
    total = 0
    for i in range(n):
        total += i * arr[i]

    if total > best:
        best = total           # naya record

print(best)    

