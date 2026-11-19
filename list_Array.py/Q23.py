# Q.23) Python program to find nearest lesser and greater element in array
# Given an array of N elements and we have to find nearest lesser and nearest greater element using C program.


############################# DOUT HAI ################################

arr = [10, 4, 7, 15, 20]
num = 8
lesser = None                 
greater = None                 

for x in arr:
    if x < num:
       
        if lesser is None or x > lesser:
            lesser = x
    elif x > num:
       
        if greater is None or x < greater:
            greater = x
   

if lesser is None:
    print("No lesser element")
else:
    print("Lesser =", lesser)      

if greater is None:
    print("No greater element")
else:
    print("Greater =", greater)  












