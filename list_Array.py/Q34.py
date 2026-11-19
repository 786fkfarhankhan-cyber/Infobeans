# 34.
# Write a Python program to implement linear search


arr = [7, 9, 2, 5, 6, 4, 1]
target = 6
found = False                         

for i in range(len(arr)):            
    if arr[i] == target:              
        print(target, "found at index", i)
        found = True
        break                       

if found == False:                  
    print(target, "not found")