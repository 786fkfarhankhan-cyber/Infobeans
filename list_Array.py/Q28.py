# 28.
# P is one-dimensional array of integers. Write a Python program search for a data VAL from P. If VAL is present in the array then “element found ” otherwise “element not found” should be displayed.


P = [7, 9, 2, 5, 6, 4, 1]
VAL = int(input("Enter VAL: "))   # jise dhundhna hai

found = False                      # abhi tak nahi mila

for x in P:
    if x == VAL:                   # match mila
        found = True
        break                      # ab aage dekhne ka faayda nahi

# loop khatam hone ke baad faisla
if found == True:
    print("element found")
else:
    print("element not found")









