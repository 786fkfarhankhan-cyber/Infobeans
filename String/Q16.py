# 16. Check whether two strings are anagrams.
# Example: "listen" and "silent" → True

s1 = "lisen"
s2 = "silen"

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("not Anagrams")






