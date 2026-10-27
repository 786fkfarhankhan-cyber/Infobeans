# 24. Reverse every word without changing the word order.
# Example: "Python is easy" → "nohtyP si ysae"

s = input("Enter a String = ")

words = list(s.split(" "))       
for word in words:
    print(word[::-1],end=" ")








