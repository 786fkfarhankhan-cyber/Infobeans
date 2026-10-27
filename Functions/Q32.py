# 32. Find the longest palindromic substring.
# Example: "babad" → "bab" or "aba"
def palindrome():
    s = "babad"

    t = s[0:3]
    if t == t[::-1]:
        print("palindrome ")
    else:
        print(" not palindrome ")
palindrome()