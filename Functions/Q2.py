# 2. Check whether a string is a palindrome. Using Function
# palindrome = madam -> madam same hi rhe reverse ke baad bhu
def palindrome(sr):
    # sr = input("Enter a String = ")
    pal = ""
    for ch in sr:
        pal = ch + pal
    if pal==sr:
        print("It is Palindrome")
            
    else:
        print("It not a Palindrome")
            
sr = input("Enter a String = ")
palindrome(sr)









