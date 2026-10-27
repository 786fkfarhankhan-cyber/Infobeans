# 23. Reverse the order of words in a sentence.
# Example: "Python is easy" → "easy is Python"

def reverse():

    s = input("Enter a String = ")

    words = list(s.split(" "))         
    words.reverse()            
    result = " ".join(words)
    return result

re = reverse()
print(re)