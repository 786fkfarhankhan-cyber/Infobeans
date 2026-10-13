# Q.14
# Find the first repeating element in array of integers

arr=[1,5,3,5,7,3,6,9]
found=None
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i]==arr[j]:
            found=arr[i]
            break
        
    if found is not None:
        break
if found is not None:
    print(found)
else:
    print("no repeating element  ")