# Right Diagonal 
# x = [[1,2,3],
#      [4,5,6],
#      [7,8,9]] 
# a = 0
# b = len(x[0])-1 # last column index 
# for r in range(len(x)):
#     for c in range(len(x[r])):
#         if r == a and c == b:
#             print(x[r][c])
#             a+=1
#             b-=1
#         else:
#             print("0",end=" ")
#     print()







# Left Diagonal 
# x = [[1,2,3],
#      [4,5,6],
#      [7,8,9]] 
# for r in range(len(x)):
#     for c in range(len(x[r])):
#         if r==c:
#             print(x[r][c],end=" ")
#         else:
#             print(" ",end=" ")
#     print()

          ### OR ###

# x = [[1,2,3],
#      [4,5,6],
#      [7,8,9]] 
# for r in range(len(x)):
#     for c in range(len(x[r])):
#         if r==c:
#             print(x[r][c])



