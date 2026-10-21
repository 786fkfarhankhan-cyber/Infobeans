# Q.21 Longest consecutive sequence.
# Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.


arr = [1, 9, 3, 10, 4, 20, 2]
n = len(arr)
for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
longest = 1                    
current = 1                   
for i in range(1, n):
    if arr[i] == arr[i - 1] + 1:
        current += 1           
    elif arr[i] != arr[i - 1]:
        current = 1            
    if current > longest:
        longest = current     

print(longest)      



