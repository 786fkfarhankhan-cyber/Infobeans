# 14. Remove all digits from a string.

s = input("Enter a String = ")
result = ""

for ch in s:
    if not ch.isdigit():
        result += ch

print(result)





