# 28. Create a new dictionary containing only entries whose values are greater
#     than or equal to a given threshold. Do not modify the dictionary while
#     iterating over it.


d ={"Mango":90,"Apple":60,"Berry":43,"Graphes":21}

threshold = float(input("Enter a Threshold Limit = "))
data = {}

for key,value in d.items():
    if value>=threshold:
        data[key]=value
print(data)






