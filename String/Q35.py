# 35. Expand a compressed string.
# Example: "a3b2c4" → "aaabbcccc"

s = "a4b3c2d"
word = ""
ans = ""
for ch in s:
    if ch.isdigit():
        ans +=word*int(ch)
        word = ""
    else:
        word+=ch
ans+=word        
print(ans)    







