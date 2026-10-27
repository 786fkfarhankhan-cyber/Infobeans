# 28. Check whether one string is a rotation of another. By Function
# Example: "abcd" and "cdab" → True
def rotate():
    s1 = "abcd"
    s2 = "cdab"

    if len(s1) == len(s2) and s2 in s1 + s1:
        print("True")
    else:
        print("False")
rotate()

