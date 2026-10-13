m = [ [1,2,3,4] ,
     [5,6,8,9],
     [2,6,7,8]
     ]
max_sum = 0
max_row = 0
min_sum = 0
min_index = 0 
for row in range(len(m)):
    sum = 0
    
    for element in m[row]: 
        sum = sum+element

    if max_sum <sum:
        max_sum = sum
        max_row = row
    if min_sum>sum:
        min_sum = sum
        min_index = row
m[min_index],m[max_row] = m[max_row],m[min_index]
print(m)
