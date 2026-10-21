# 30. Safely retrieve a value from a deeply nested dictionary. If any key is
#     missing, return a default value such as "Unknown".

students = {
    "std1":{
        "name":"Farhan",
        "age":21,
        "marks":{
            "other":88,
            "softskills":75,
            "technical":56
        }
    },
    "std2":{
        "name":"ram",
        "age":23,
        "marks":{
            "other":96,
            "softskills":56,
            "technical":80
        }
    },
    "std3":{
        "name":"dev",
        "age":33,
        "marks":{
            "other":55,
            "softskills":74,
            "technical":45
        }
    }
}

search_key = "marks"
val=0
for key,value in students.items():
    if(key == search_key) or (search_key in value):
        val = key 
        break
if val:
    print("Key founded")
else:
    print("key not founded")













