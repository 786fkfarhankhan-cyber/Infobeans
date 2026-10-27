# 20. Remove duplicate characters while preserving their original order.
# Example: "programming" → "progamin"
s = "programming"
result = ""

for i in s:
    if i not in result:
        result+=i
        print(i,end="")
    











