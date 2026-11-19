# 36.
# Write a Python program to implement bubble sort algorithm

nums = [5, 1, 4, 2]
n = len(nums)

for i in range(n - 1, 0, -1):       
    for j in range(i):             
        if nums[j] > nums[j + 1]:   
            nums[j], nums[j + 1] = nums[j + 1], nums[j]   

print(nums)           