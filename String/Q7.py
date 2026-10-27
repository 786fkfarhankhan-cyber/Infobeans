# 7. Convert lowercase characters to uppercase without using upper().
#   s = "inDor434e"  => "INDOR434E"


s = "Hello786 World i will save you"

for i in s:
    
    if ord(i)>=97 and ord(i)<=122:
        v = chr(ord(i)-32)
        print(v,end="")
    else:
        print(i,end="")






