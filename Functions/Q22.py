# 22. Find the second most frequent character.

def sec_frequent_chr():
    s = "Prrogramminp"
    d={}
    max_count = 0
    max_char = ""
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i] > max_count: 
            max_count = d[i]  # d[i] uski value h  d[name] = "Farhan"
            max_char = i  # i character h yani key
    print(f"Max Count = {max_count}, Max Chracter = {max_char}")

    second_count = 0
    second_char = ""
    for i in d:
        if i == max_char:
            continue
        if d[i] > second_count:
            second_count = d[i]
            second_char = i

    print(f"Second Chracter Occur Maximum Time = {second_char}")

sec_frequent_chr()





