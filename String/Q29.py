# 29. Remove a particular character from a string without using replace().

# s = "Because of my decision i trap"
# print(s)
# remo = input("Enter a character you want to remove = ")
# li = list(s)
# li.remove(remo)
# print("".join(li))

s = "Because of my decision i trap"
remo = input("Enter a character you want to remove = ")

result = ""
for ch in s:
    if ch != remo: # Agar character not equal remove h to result me plus kardo
        result += ch

print(result)
