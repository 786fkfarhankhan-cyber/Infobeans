# 19. Find all duplicate elements in a list and their frequencies.


d={}
s = input("Enter ur Stiring = ")
l = list(s)
d = {i:l.count(i) for i in l if l.count(i) >1 }
print(d)


# l = ["saiya", "you", "saiya", "axs", "you", "saiya"]
# d = {i: l.count(i) for i in l if l.count(i) > 1}
# print(d)   




