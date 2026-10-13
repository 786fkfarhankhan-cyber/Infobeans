# Q.7 Sort the array of 0s , 1s and 2s.
arr =    [0,0,1,2,2,1,0,2,1,1]
# Index = 0 1 2 3 4 5 6 7 8 9
low = 0
mid = 0
high = 9
while mid<=high:
    if arr[mid]==1:
        mid+=1
    elif arr[mid] == 0:
        arr[low],arr[mid] = arr[mid],arr[low]
        low +=1
        mid +=1
    else:
        arr[high],arr[mid] = arr[mid],arr[high]
        high -=1
print(arr)
