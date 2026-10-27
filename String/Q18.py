# 18. Find the first repeating character.
# Example: "programming" → r
s = "programming"
r = {}

for i in s:
    if i in r:
        r[i] += 1
    else:
        r[i] = 1

for i in s:
    if r[i] > 1:
        print(i)
        break








