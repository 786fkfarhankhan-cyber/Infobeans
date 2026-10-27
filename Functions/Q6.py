# 6. Find the length of a string without using len() Using Function.
def length(s):
    # s = "ywdj sbxjscbjs"
    count = 0
    word = s.split(" ")

    for i in word:
        count+=1
    
    print(count)
s = input("Enter Sentence = ")
length(s)