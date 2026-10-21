# 34. Predict the output:

    
data = {"name":"Farhan", "age":21}
data_new = data
data_new["name"]="ALi"
# o/p will also update the data dictionary because the concept of shallow copy
print(data)