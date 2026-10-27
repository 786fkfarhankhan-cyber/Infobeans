# 16. Check whether two strings are anagrams. by Function
# Example: "listen" and "silent" → True

def anagrams():

    s1 = "lisen"
    s2 = "silen"

    if sorted(s1) == sorted(s2):
        print("Anagrams")
    else:
        print("not Anagrams")

anagrams()




