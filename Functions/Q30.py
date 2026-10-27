# 30. Find the longest common prefix among a list of strings.
# Example: ["flower", "flow", "flight"] → "fl"

def prefix():
    s = ["flower", "flow", "flight"]
    first = s[0]
    ans = ""
    for i in range(len(first)):
        for j in range(1,len(s)):
            if i>=len(s[j]) or first[i]!=s[j][i]:
                break
        else:
            ans+=first[i]
            continue
        break
    print(ans)     
prefix()








