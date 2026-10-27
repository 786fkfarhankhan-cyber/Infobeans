# 31. Find the longest substring without repeating characters.
# Example: "abcabcbb" → 3 ("abc")


# t = "abcabcbb"

# seen = ""
# rep = False

# for ch in t:
#     if ch in seen:
#         repeat = ch
#         rep = True

#         break
#     seen += ch

# print(seen,"\n Repeating Chracter = ",repeat)

s = "abcdabcdbb"
left = right = 0
ans = set()
maxx = 0
for right in range(len(s)):
    ch = s[right]
    while ch in ans:
        ans.remove(s[left])
        left+=1
    ans.add(ch)       
    maxx = max(maxx,right-left+1) 
print(f"The longest substring without repeating characters : {maxx}")





