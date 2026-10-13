# Write a program to cyclically rotate array by one.

arr = [10,20,30,40,50]
item = arr[-1]
for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
arr[0] = item
print(arr)