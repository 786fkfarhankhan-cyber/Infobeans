# Find it there is any subarray with sum equals to zero
# Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

arr = [4, 2, -3, 1, 6]
found = False                  

for i in range(len(arr)):     
    total = 0                 
    for j in range(i, len(arr)):   
        total += arr[j]        
        if total == 0:         
            found = True
            break              
    if found:
        break                 

if found:
    print("Yes")
else:
    print("No")