password = input("Enter the Password = ")

length = len(password)
attempt = 0

if attempt<3:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

for ch in password:
    if ch.isupper():
        has_upper=True
    elif ch.islower():
        has_lower=True
    elif ch.isdigit():
            has_digit=True
    else:
            has_special = True

if length>=8 and has_upper and has_lower and has_digit and has_special:
    print("Stron Password")
elif length<6 and (has_upper or has_lower) and (has_digit or has_special):
    print("Medium password")
else:
     print("Weak Password")












