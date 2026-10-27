# 11. Count how many times a particular character occurs. Using Function
def chr_occur():

    s = input("Enter the string = ")
    d = {}
    for ch in s:
        if ch in d:
            d[ch]+=1
        else:
            d[ch]=1
    print(d)

chr_occur()
