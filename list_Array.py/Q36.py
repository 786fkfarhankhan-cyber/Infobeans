# 36.
# Write a Python program to implement bubble sort algorithm

nums = [5, 1, 4, 2]
n = len(nums)

for i in range(n - 1, 0, -1):       # i = abhi ka aakhri index jahan tak dekhna hai
    for j in range(i):              # j = 0 se i-1 tak, jodi (j, j+1) dekhte hain
        if nums[j] > nums[j + 1]:   # left wala bada hai?
            nums[j], nums[j + 1] = nums[j + 1], nums[j]   # to swap

print(nums)           