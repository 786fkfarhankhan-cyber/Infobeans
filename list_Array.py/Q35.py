# 35.
# Write a Python program to implement selection sort algoritm

nums = [29, 10, 14, 37, 13]
n = len(nums)

for i in range(n - 1):              # i = jis position pe sabse chhota rakhna hai
    min_ind = i                     # maan lo yahi sabse chhota hai (index yaad rakha)

    for j in range(i + 1, n):       # i ke aage ke sab dekho
        if nums[j] < nums[min_ind]: # isse bhi chhota mila?
            min_ind = j             # to uska index yaad kar lo (swap abhi nahi)

    # sabse chhota mil gaya, ab ek hi swap
    nums[i], nums[min_ind] = nums[min_ind], nums[i]

print(nums)        

