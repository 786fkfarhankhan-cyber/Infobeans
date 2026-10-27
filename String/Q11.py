# 11. Count how many times a particular character occurs.

s = input("Enter the string = ")
d = {}
for ch in s:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print(d)






