# 29. Given two dictionaries, return the keys whose values are equal in both.

same_value_list = []
d1 = {"name":"Saniya","city":"Godhra" ,"age":21, "mob":895686743}
d2 = {"name":"Alsifa","city":"Ramganjmandi", "age":23}
if len(d1)>len(d2):
    for key,value in d1.items():
        if key in d2 and d2[key]==value:
            same_value_list.append(key)
print(same_value_list)








