# 32. Find the longest palindromic substring.
# Example: "babad" → "bab" or "aba"

s = "babad"

t = s[0:3]
if t == t[::-1]:
    print("palindrome ")
else:
    print(" not palindrome ")





