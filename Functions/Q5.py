# 5. Count the number of words in a sentence. Using Function
def word_count(s):
    count=0
    l=s.split()
    for word in l:
        count+=1
    return count

s = input("Enter a str = ")
v = word_count(s)
print(v)




