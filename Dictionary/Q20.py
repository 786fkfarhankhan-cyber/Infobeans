# 20. Reverse a dictionary so that values become keys and keys become values.
#     Assume all values are unique.

# always remeber fer key aur value ko inter change krne ke liye nayi dictionary banana
d = { "name" : "Farhan",
     "Class" : 10 ,
     "student" : 43 ,
     "avg_age" : 21}
new = {}
for k,v in d.items():
    new[v]=k

print(new)

############ OR ###########


# new = {v: k for k, v in d.items()}
# print(new)











