# 9. Find the key associated with the largest value in a dictionary.

num = {"student" : 50 ,
       "age" : 80,
       "sub" : ("Math","Science","Python","Strategy")
       }
max_value = 0

for key,value in num.items():
    a = str(value)
    if a.isdigit():
        a = int(value)
        if max_value < a:    
            max_value = a    
            max_key = key 
print(max_key,max_value)

        
    
















