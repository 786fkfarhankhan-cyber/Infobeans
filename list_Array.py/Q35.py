# 35.
# Write a Python program to implement selection sort algoritm

nums = [29, 10, 14, 37, 13]
n = len(nums)

for i in range(n - 1):              
    min_ind = i                     

    for j in range(i + 1, n):       
        if nums[j] < nums[min_ind]: 
            min_ind = j            

    
    nums[i], nums[min_ind] = nums[min_ind], nums[i]

print(nums)        

