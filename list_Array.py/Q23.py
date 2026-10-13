# Q.23) Python program to find nearest lesser and greater element in array
# Given an array of N elements and we have to find nearest lesser and nearest greater element using C program.


############################# DOUT HAI ################################

arr = [10, 4, 7, 15, 20]
num = 8
lesser = None                  # num se chhote mein sabse bada
greater = None                 # num se bade mein sabse chhota

for x in arr:
    if x < num:
        # x chhota hai. pehla mila ya pichle lesser se bada hai?
        if lesser is None or x > lesser:
            lesser = x
    elif x > num:
        # x bada hai. pehla mila ya pichle greater se chhota hai?
        if greater is None or x < greater:
            greater = x
    # x == num ho to kuch nahi karna

if lesser is None:
    print("No lesser element")
else:
    print("Lesser =", lesser)       # 7

if greater is None:
    print("No greater element")
else:
    print("Greater =", greater)  












