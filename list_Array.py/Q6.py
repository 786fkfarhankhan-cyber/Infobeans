# Q.6 Find occurance of an integer number in array.

arr = [3,4,5,6,4,9,8]
x = int(input("Enter a no you want to find = "))
count = 0
for i in arr:
    if i == x :
        count+=1
print(x,"Occur",count,"Times")