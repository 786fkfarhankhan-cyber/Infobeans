# 26. Check whether a string contains only digits without using isdigit().
s = input("Enter a String = ")
dig = "1234567890"
is_digit = True

for i in s:
    if i not in dig:        
        is_digit = False
        break

if is_digit:
    print("Only digits")
else:
    print("Not only digits")

