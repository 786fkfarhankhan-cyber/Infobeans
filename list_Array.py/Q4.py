# Q.4 Write a program to sort the array
arr = [3,4,5,8,10,6,7]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)