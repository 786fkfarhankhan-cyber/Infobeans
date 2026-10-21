# 10. Merge two dictionaries. If a key exists in both dictionaries, use the
#     value from the second dictionary.
n1 = {"name":"Farhan", "class":"Infobeans","strength" : 43}

n2 = {"name":"Khan", "class":"Infobeans","strength" : 46,"city": "Indore"}

# n1.update(n2)
# print(n1)
a = n1|n2
print(a)


