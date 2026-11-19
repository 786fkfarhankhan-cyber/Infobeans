# 26.
# Write a Python program to reverse the element of an integer 1-D array.

arr = [4, 8, 9, 1, 8, 7, -100, 100, 2, 23]

largest = arr[0]          
smallest = arr[0]        

for x in arr:
    if x > largest:      
        largest = x
    if x < smallest:      
        smallest = x

print("Largest =", largest)      
print("Smallest =", smallest)    


