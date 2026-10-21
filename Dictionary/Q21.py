
# 21. Combine two dictionaries by adding the values of common keys.
#     Example: {'a': 10, 'b': 20} and {'b': 5, 'c': 7}
#     Expected: {'a': 10, 'b': 25, 'c': 7}


d1 = {'a': 10, 'b': 20}
d2 = {'b': 5, 'c': 7}
result = d1.copy() # ye copy isliye kra kyuki original dictionary ki values change na ho
for key, value in d2.items(): # kyuki hum d1 ko d2 me jor rhe h  ulta bhi kar sakte h result = d2.copy() fir d1.items() in loop
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)






