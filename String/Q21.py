# 21. Find the most frequent character in a string.

s = "Programming"
d={}
max_count = 0
max_char = ""
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    if d[i] > max_count: 
        max_count = d[i]  # d[i] uski value h  d[name] = "Farhan"
        max_char = i   # i character h yani key
print(max_count,max_char)


