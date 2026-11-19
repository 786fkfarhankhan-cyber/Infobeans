# Q.22 Max Sum in configuration
# Given an array(0-based indexing), you have to find the max sum of i*A[i] where A[i] is the element at index i in the array.The only operation allowed is to rotate(clock-wise or counter clock-wise) the array any number of times.

arr = [8, 3, 1, 2]
n = len(arr)


best = 0
for i in range(n):
    best += i * arr[i]


for r in range(n):
  
    item = arr[-1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = item

  
    total = 0
    for i in range(n):
        total += i * arr[i]

    if total > best:
        best = total           

print(best)    

