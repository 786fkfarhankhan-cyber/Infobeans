# 37.
# Write a Python progrtam to implement insertion sort algorithm


nums = [5, 2, 4, 1]

for i in range(1, len(nums)):       # i = agla patta (index 0 pehle se sorted maan lo)
    key = nums[i]                   # patta haath mein uthaya
    j = i - 1                       # sorted hisse ka aakhri index

    while j >= 0 and nums[j] > key: # peeche jaao jab tak bade patte mil rahe hain
        nums[j + 1] = nums[j]       # bade patte ko ek jagah daayein khiskao
        j -= 1                      # ek aur peeche dekho

    nums[j + 1] = key               # khali jagah mein key rakh do

print(nums)           
