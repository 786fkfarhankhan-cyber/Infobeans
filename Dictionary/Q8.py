# 8. Calculate the sum of all numeric values in a dictionary. 
# list se karke dekhna h

# num = {"student" : 50 ,
#        "age" : 80,
#        "sub" : ("Math","Science","Python","Strategy")
#        }
# sum = 0
# for key,value in num.items():
#     a = str(value)
#     if a.isdigit():
#         sum+=value

# print(sum)


num = {"student" : [1,2,3,4,5,6] ,
       "age" : (21,22,23,21,20,19),
       "sub" : ("Math","Science","Python","Strategy")
       }
for key, value in num.items():
    if isinstance(value, (list, tuple)):
        total = 0
        found = False
        for n in value:
            if isinstance(n, (int, float)):
                total += n
                found = True
        if found:
            print(key, "=", total)