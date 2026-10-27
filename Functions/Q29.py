# 29. Remove a particular character from a string without using replace(). By Function
def rep(s, remo):
    result = ""
    for ch in s:
        if ch != remo:
            result += ch
    return result

s = "Because of my decision i trap"
print(s)
remo = input("Enter a character you want to remove = ")
print(rep(s, remo))