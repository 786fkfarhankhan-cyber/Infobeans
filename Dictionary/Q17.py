# 17. Count the frequency of each number in a list.
#     Example: [1, 2, 2, 3, 1, 2] -> {1: 2, 2: 3, 3: 1}

l = [1, 2, 2, 3, 1, 2]
d={i:l.count(i) for i in l}

print(d)















