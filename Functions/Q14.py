# 14. Remove all digits from a string.
def digit(s):
    
    result = ""

    for ch in s:
        if not ch.isdigit():
            result += ch
    return result
s = input("Enter a String = ")
print(digit(s))
