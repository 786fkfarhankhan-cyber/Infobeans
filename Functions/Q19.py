# 19. Count the frequency of every character using a dictionary. By Function
# Example: "hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1}

def frequency(s):
    # s = input("Enter a String = ")
    r = {}

    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    return r
s = input("Enter a String = ")
qw = frequency(s)
print(qw)







