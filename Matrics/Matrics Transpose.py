
#  TRANSPOSE MATRICS


b = [[1,2,3],
     [3,4,5],
     [6,7,8],
     [9,2,1]]  # 4 X 3 ka Matrix
c = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]   # 3 X 4 ka Matrix which is transpose use to store matrix
     ]

for row in range(len(c)):
    for column in range(len(c[row])):
        c[row][column] = b[column][row]
print(c)
