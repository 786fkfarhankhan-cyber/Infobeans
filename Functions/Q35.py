# 35. Expand a compressed string.
# Example: "a3b2c4" → "aaabbcccc"

def expand(s):

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
s = "a4b3c2d"
com = expand(s)
print(com)





