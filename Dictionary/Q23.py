
# 23. Sort a dictionary by its values in ascending order.
e = {}
d = {"stu" : 1101,
     "Age" : 20
    }

key_var = 0
for _ in range(len(d)):
    min = 100000
    for key,value in d.items():
        if min>=value:
            min=value
            key_var=key
    e[key_var] = min
    del d[key_var]
print(e)