# WAP to reverse matric
b = [[1,2,3],
     [3,4,5],
     [6,7,8],
     [9,2,1]]
for row in b:
    start = 0
    end = 2     # column 0,1,2
    while start<end:
        row[start] , row[end] = row[end] , row[start]
        start+=1
        end-=1
print(b)
