
# 27. Find the longest word in a sentence.
s = input("Enter a String = ")
l = 0
longest = ""
word = list(s.split(" "))
for i in word:
    if len(i) > l:
        l=len(i)
        longest=i
print(longest, " = ",l)








