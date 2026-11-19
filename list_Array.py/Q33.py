# 33.
# Write a Python program to impelment binary search algorithm

arr = [2, 4, 6, 7, 9, 11, 18, 19]     
target = 11

low = 0                  
high = len(arr) - 1     
found = False

while low <= high:
    mid = (low + high) // 2           
    if arr[mid] == target:           
        print(target, "is on index", mid)
        found = True
        break
    elif arr[mid] < target:           
        low = mid + 1                 
    else:                            
        high = mid - 1               

if found == False:
    print("not found")
