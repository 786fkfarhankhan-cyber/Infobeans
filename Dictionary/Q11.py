# 11. Create a dictionary from two lists: one list contains keys and the
#     other contains values. Do not use zip().
l1 = ["name","age","marks","city"] 
l2 = ["Farhan",21.10,75,"Indore"]
di = { l1[i]:l2[i] for i in range(len(l1)) } # l1[i] = yani key  ,  l2[i] = yani value
print(di)












