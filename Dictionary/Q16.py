# 16. Count the frequency of each character in a string.
#     Example: "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# s = input("Enter your string = ")
# d={}
# for ch in s:
#     if ch in d:
#         d[ch]+=1
#     else:
#         d[ch]=1

# print(d)



s = input("Enter your string = ")
d = {ch: s.count(ch) for ch in s}
print(d)





