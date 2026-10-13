# 34.
# Write a Python program to implement linear search


arr = [7, 9, 2, 5, 6, 4, 1]
target = 6
found = False                         # abhi tak nahi mila

for i in range(len(arr)):             # i = index, 0 se aakhir tak
    if arr[i] == target:              # is dibbe mein wahi number hai?
        print(target, "found at index", i)
        found = True
        break                         # mil gaya, ruk jao

if found == False:                    # poora dekha, nahi mila
    print(target, "not found")