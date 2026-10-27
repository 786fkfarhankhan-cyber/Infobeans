# 18. Find the first repeating character. by Function 
# Example: "programming" → r

def first_repeating(s):
    # s = "programming"
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

s = input("Enter a String = ")
er = first_repeating(s)

print(er)



