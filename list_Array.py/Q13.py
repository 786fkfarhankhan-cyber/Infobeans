# Find common elements in three sorted arrays.
# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?


arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

i = 0                  # arr1 pe ungli
j = 0                  # arr2 pe ungli
k = 0                  # arr3 pe ungli
result = []            # common numbers yahan jama honge

# tab tak chalo jab tak teeno arrays mein kuch bacha ho
while i < len(arr1) and j < len(arr2) and k < len(arr3):

    if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
        # teeno barabar -> common mil gaya
        if not result or result[-1] != arr1[i]:   # duplicate na jaye
            result.append(arr1[i])
        i += 1         # teeno ungliyan aage
        j += 1
        k += 1

    elif arr1[i] < arr2[j]:
        i += 1         # arr1 wala chhota hai, common nahi ho sakta

    elif arr2[j] < arr3[k]:
        j += 1         # arr2 wala chhota hai

    else:
        k += 1         # baaki case mein arr3 wala sabse chhota hai

print(result)          # [20, 80]


