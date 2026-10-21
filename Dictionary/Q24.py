# 24. Group a list of words according to their length.
#     Example: ["cat", "apple", "dog", "mango"]
#     Expected groups: 3 -> ["cat", "dog"], 5 -> ["apple", "mango"]

l = ["cat", "apple", "dog", "mango"]
result = {len(element):[] for element in l}
print(result)
for element in l:
    result[len(element)].append(element)
print(result)





