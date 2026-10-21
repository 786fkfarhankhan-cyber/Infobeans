# 2. Check whether a string is a palindrome.
# palindrome = madam -> madam same hi rhe reverse ke baad bhu
sr = input("Enter a String = ")
pal = ""
for ch in sr:
    pal = ch + pal
if pal==sr:
    print("It is Palindrome")
        
else:
    print("It not a Palindrome")
        
print(pal)





