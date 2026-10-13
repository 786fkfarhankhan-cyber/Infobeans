# Find it there is any subarray with sum equals to zero
# Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

arr = [4, 2, -3, 1, 6]
found = False                  # abhi tak zero-sum subarray nahi mila

for i in range(len(arr)):      # subarray kahan se shuru
    total = 0                  # naya start, sum 0 se
    for j in range(i, len(arr)):   # kahan tak badhe
        total += arr[j]        # naya element sum mein jodo
        if total == 0:         # sum zero mil gaya
            found = True
            break              # inner loop band
    if found:
        break                  # bahar wala loop bhi band

if found:
    print("Yes")
else:
    print("No")