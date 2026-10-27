# 17. Find the first non-repeating character in a string. By Function
# Example: "aabbcddee" → c

def non_repeating():
    s = "aabbcddee"
    r = {}

    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1

    for i in s:
        if r[i] == 1:
            print(i)
            break
non_repeating()


