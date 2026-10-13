# Mutable
# Ordered
# Contain duplicate
# hetro+homo
# support silicing , indexing
# overallocation
# nested list


# x =[10,"hello",True,100]
# for i in x:
#     print(i)
#    print(len(x))
# for i in range(len(x)): ### Index by loop
#     print(x)
#     # print(x[i])


# x =[10,20,30,40]
# print(f"Length of list {len(x)}")
# print(f"Type of list {type(x)}")
# print(f"Element of list {x}")

# # Index Basis
# for i in range(len(x)):
#     print(f"Index : {i} ---> value : {x[i]}")

# # Element 
# for ele in x:
#     print(f"Element ---> {ele}")


#    -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# l1 = [10,20,30,40,50,60,70,80,90,100] # l1 ref. variable aur list ke andar jo element h wo object
#     0  ,1 ,2, 3, 4, 5 ,6 ,7 ,8 ,9

# print(f"len : {len(l1)}")
########################################### Silicing in List #############################################
# print(l1[2:5])
# print(l1[1:7]) # 1 start se 6 tak
# print(l1[1:100])
# print(l1[1:7:2]) # star 1 stop 7 step 2
# print(l1[2:])
# print(l1[:8])
# print(l1[-3:])
# print(l1[-8::2])
# print(l1[-8:-4])
# print(l1[::-1])   # reversing 
# print(l1[7:3:-1]) 
# print(l1[::2])  # skip element

######################################## Insert Method of list ################################################
# if step is negative then start index should be greater then ending index
# if step is positive then start index should be smaller then ending index

# if negative index not avalable then it will insert at the start
# l1.insert(-50,101)
# if positive index not avalable then it will insert at the end
# l1.insert(50,220)
# print(l1)

# for i in range(len(l1)):
#     print(f"Index : {i} .... value : {l1[i]}")



################################# Extend Method of List #######################################

# l1 = [10,20,30,40,50,60,70,80,90,100]
# l1.extend([3000,9000])
# print(l1)

# l1 = [1,2,3]
# l2 = [4,5,6]
# l1.append(l2) 
# print(l1)
# l1.extend(l2) # Use when multiple element are there
# print(l1)


############################################ Updating of List ###############################################

#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# l1 =   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         0,1,2,3,4,5,6,7,8,9

# print(l1)
# l1[-3] = 500
# print(l1)


# l1[2:6] = ["A","B","C","D"]
# print(l1)


# a = [10,20,30]
# print(a)
# a[:] = [1,2,3,4,5]
# print(a)


###################################### Remove , PoP, Clear , Del ######################################

# * Remove = the first occurence of element through object
# * POP = removes the element at a specific index or the last element if no index is specific
# * Clear = Remove all element from list
# * Del = Specific element , Multiple element , Entire list 


# l = [1,2,3,4,5]

# Remove()

# print(l)
# l.remove(2)
# print(l)


# pop()

# print(l)
# l.pop(3)
# print(l)

# del()

# print(l)
# del l[1:4:2]
# print(l)



# Clear()
# print(l)
# l.clear()
# print(l)




# ---------------------------------------- Date = 25/09/26 (Friday) -------------------------------------------




# li = [5,4,3,2,1]
# sum = 0 
# for element in li:
#     sum = sum + element
# print(sum)


# li = [5,4,3,2,11]
# even = 0 
# odd = 0
# for element in li:
#     if element in li:
#         even = even+element
#     else:
#         odd=odd+element
    
# print(even , odd)


### TWO POINTER PROBLEM ###
# arr1 = [2,3,3,4,5]
# arr2 = [1,3,4,4,6,7,8]
# result=[]
# i=0
# j=0
# while (i<len(arr1)) and (j<len(arr2)):
#     if arr1[i] < arr2[j]:
#         result.append(arr1[i])
#         i+=1
#     else:
#         result.append(arr2[j])
#         j+=1

# while i<len(arr1):
#     result.append(arr1[i])
#     i+=1
# while j<len(arr2):
#     result.append(arr2[j])
#     j+=1
# print(result)

# print(f"arr1 : {arr1}")
# print(f"arr2 : {arr2}")


#****************************************** DATE - 28/09/2026 **************************************************

### Two Sum Problem (Leet Code) ###
# arr = [1,5,6,8,7,9]
# target = 12
# result = []
# flag = False
# for i in range(len(arr)-1):
#     for j in range(i+1 , len(arr)):
#         if(arr[i]+arr[j])==target:
#             result.extend([i,j])
#             print(result)
#             break
#     if result:
#         break


# arr = [2,7,11,15]
# i= 0
# target = 9
# j= len(arr)-1
# while i<j:
#     sum = arr[i] + arr[j]
#     if sum == target:
#         result = [i,j]
#         print(result)
#         break
#     elif sum>target:
#         j-=1
#     else:
#         i+=1



# ****************************************** DATE = 29/09/26 *************************************

### List Comprehension

# 1 Creation 
# 2 Transformation 
# 3 Filteration









