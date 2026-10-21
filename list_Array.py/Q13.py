# Find common elements in three sorted arrays.
# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?


arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

i = 0                  
j = 0                  
k = 0                  
result = []           


while i < len(arr1) and j < len(arr2) and k < len(arr3):

    if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
        
        if not result or result[-1] != arr1[i]:   
            result.append(arr1[i])
        i += 1        
        j += 1
        k += 1

    elif arr1[i] < arr2[j]:
        i += 1         

    elif arr2[j] < arr3[k]:
        j += 1         

    else:
        k += 1         

print(result)          


