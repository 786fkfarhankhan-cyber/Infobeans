# 27. Group words that are anagrams of one another.
#     Example: ["eat", "tea", "bat", "ate"]
#     Expected groups: ["eat", "tea", "ate"] and ["bat"]


data_list = ["eat", "tea", "bat", "ate", "potato", "naman", "anman"]
res = {}
for word in data_list:
    val = "".join(sorted(word))
    if val in res:
        res[val].append(word)
    else:
        res[val] = [word]
print(list(res.values()))


print("\n")








