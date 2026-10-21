# Q.20) Find Maximum product contigeous sub array
# Given an array Arr[] that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.


arr = [6, -3, -10, 0, 2]
best = arr[0]                

for i in range(len(arr)):      
    product = 1               
    for j in range(i, len(arr)):
        product = product * arr[j]  
        if product > best:
            best = product     

print(best)    