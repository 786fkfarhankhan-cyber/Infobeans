# 25. Given a nested dictionary of students and their subject marks, calculate
#     each student's total marks and find the topper.

g = {"s1":{"name" : "fhe","marks":[20,68,48]},
     "s2" : {"name" : "kp","marks":[54,89,23]},
     "s3" : {"name" : "Laksh","marks":[90,34,69]}}
val=0
for key,value in g.items() :
    topper=0
    for ele in value["marks"]: # yani marks me jo values h wo
        val+=ele  # val ke andar element wise add kar rhe h
    if val>topper: # agar value jada h topper ki to hum topper ko val ki value assign kar dege
        topper=key
        

print(topper)
        





