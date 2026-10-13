# Q.19) Find largest sum contigeous sub array
# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

arr = [1, 2, 3, -2, 5]
current = arr[0]               # abhi tak ka running sum (pehle element se shuru)
best = arr[0]                  # ab tak ka sabse bada sum

for i in range(1, len(arr)):   # dusre element se chalo
    if current < 0:
        current = arr[i]       # pichla sum bojh tha, naya subarray yahin se
    else:
        current = current + arr[i]   # pichle ke saath jod lo
    if current > best:
        best = current         # naya record

print(best)   


















