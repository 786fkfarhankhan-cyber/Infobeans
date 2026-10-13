# Q15
# First Non Repeating Element
arr = [-1,2,6,3,-1,3,2]
found = 0
for i in range(len(arr)):
    repeating = False

    for j in range(len(arr)):
        if i != j and arr[i] == arr[j]:
            repeating = True
            break
    if repeating == False:
        found = arr[i]
        break
print(found)
