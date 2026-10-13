# Q.8 Sub array with given sum
arr = [1,2,3,7,5]
target = 12
left = 0
current_sum = 0
found = 0 # Flag variable h

for right in range(len(arr)):
    current_sum=current_sum+arr[right]

    while current_sum>target and left<=right:
        current_sum = current_sum - arr[left]
        left+=1

    if current_sum == target:
        print(left+1,right+1)
        found = True
        break

if found == False:
    print("-1")





