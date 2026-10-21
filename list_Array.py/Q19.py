# Q.19) Find largest sum contigeous sub array
# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

arr = [1, 2, 3, -2, 5]
current = arr[0]               
best = arr[0]                 

for i in range(1, len(arr)):   
    if current < 0:
        current = arr[i]       
    else:
        current = current + arr[i]   
    if current > best:
        best = current         

print(best)   


















