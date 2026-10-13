# Q9) Given an unsorted array arr[] of size N having both negative and positive integers. The task is place all negative element at the end of array without changing the order of positive element and negative element.

arr = [1,-1,3,2,-7,-5,11,6]
pos = []
neg = []
for element in arr:
    if element >=0:
        pos.append(element)
    else:
        neg.append(element)
arr = pos+neg
print(arr)