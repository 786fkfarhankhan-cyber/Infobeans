# 18. Find the first non-repeating character in a string using a dictionary.

s = "after you after yo"
d = {}
# for ch in s:
#     if ch in d:
#         d[ch] += 1
#     else:
#         d[ch] = 1
#         if d[ch]<2:
#             print(d)

# isme pehle character find out krna kitni bar konsa aya h fir ek reult naam ka var banaya taki usme ch ki value store kare
# agar koi chracter ek bar aya h yani wo non repeating h 
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d) 
result = 0
for ch in s:
    if d[ch] == 1:
        result = ch
        break

print(result)









