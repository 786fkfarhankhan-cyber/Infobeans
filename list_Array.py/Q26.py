# 26.
# Write a Python program to reverse the element of an integer 1-D array.

arr = [4, 8, 9, 1, 8, 7, -100, 100, 2, 23]

largest = arr[0]          # abhi tak ka sabse bada (pehla element maan liya)
smallest = arr[0]         # abhi tak ka sabse chhota (wahi pehla element)

for x in arr:
    if x > largest:       # ab tak ke bade se bhi bada mila
        largest = x
    if x < smallest:      # ab tak ke chhote se bhi chhota mila
        smallest = x

print("Largest =", largest)      # 100
print("Smallest =", smallest)    # -100


