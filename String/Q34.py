# 34. Compress a string by counting consecutive repeated characters.
# Example: "aaabbccccd" → "a3b2c4d1"


s = "aaaabbbccd"
cnt = 0
word = ""
ans = ""
for ch in s:
    if ch in word:
        cnt+=1
    else:
        if word!="":
            ans+=word+str(cnt)
        word = ch
        cnt = 1
ans+=word+str(cnt)        
print(ans)       






