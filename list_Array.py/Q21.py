# Q.21 Longest consecutive sequence.
# Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.


arr = [1, 9, 3, 10, 4, 20, 2]
n = len(arr)

# pehle sort (exchange sort, tera purana code)
for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
# ab arr = [1, 2, 3, 4, 9, 10, 20]

longest = 1                    # ab tak ki sabse lambi chain
current = 1                    # abhi chal rahi chain

for i in range(1, n):
    if arr[i] == arr[i - 1] + 1:
        current += 1           # ek zyada hai, chain badhi
    elif arr[i] != arr[i - 1]:
        current = 1            # chain tooti, nayi shuru
    # (agar barabar hai, yaani duplicate, to kuch nahi karna)
    if current > longest:
        longest = current      # naya record

print(longest)      



