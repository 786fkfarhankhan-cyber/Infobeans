# 33.
# Write a Python program to impelment binary search algorithm

arr = [2, 4, 6, 7, 9, 11, 18, 19]     # SORTED hona zaroori hai
target = 11

low = 0                  # dhundhne wale hisse ka bayan kinara
high = len(arr) - 1      # dayan kinara
found = False

while low <= high:
    mid = (low + high) // 2           # beech ka index
    if arr[mid] == target:            # mil gaya
        print(target, "is on index", mid)
        found = True
        break
    elif arr[mid] < target:           # target aage hoga
        low = mid + 1                 # bayan aadha phek do
    else:                             # target peeche hoga
        high = mid - 1                # dayan aadha phek do

if found == False:
    print("not found")
