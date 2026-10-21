# 22. Find the common keys between two dictionaries.
d1 = {'a': 10, 'b': 20}
d2 = {'b': 5, 'c': 7}

common_key = [] # ye iskeliye banaya taki common key nikale # Empty list h
for key,value in d2.items(): # key jo d2 me h
    if key in d1: # key jo d1 me bhi h
        common_key.append(key)
print(common_key)
