# 4. Count uppercase letters, lowercase letters, digits, and special characters. Using Function
def count_letters():
    st = input("Enter String = ")
    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0

    for i in range(len(st)):
        if st[i].isupper(): 
            upper_count+=1
        elif st[i].islower():
            lower_count+=1
        elif st[i].isdigit():
            digit_count+=1
        else:
            special_count+=1

    print(f"Uppercase count = {upper_count} ")
    print(f"Lowercase count = {lower_count} ")
    print(f"Digit count = {digit_count} ")
    print(f"Special count = {special_count} ")

count_letters()





