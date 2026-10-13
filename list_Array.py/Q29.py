# 29.
# Suppose a one-dimensional array AR containing integers is arranged in ascending order. Write a Python program to search for an integer from AR with the help of Binary search method,


arr = [2, 4, 6, 7, 9, 11, 18, 19]
target = 11

low = 0                       # dhundhne wale hisse ka bayan kinara (index)
high = len(arr) - 1           # dhundhne wale hisse ka dayan kinara (index)
found = False

while low <= high:            # jab tak dhundhne ke liye kuch bacha ho
    mid = (low + high) // 2   # beech ka index (// = bina decimal ka divide)

    if arr[mid] == target:    # beech mein hi mil gaya
        print(target, "is on index", mid)
        found = True
        break
    elif arr[mid] < target:   # beech wala chhota hai, target aage hoga
        low = mid + 1         # bayan aadha (mid samet) phek do
    else:                     # beech wala bada hai, target peeche hoga
        high = mid - 1        # dayan aadha (mid samet) phek do

if found == False:
    print(target, "not found")


