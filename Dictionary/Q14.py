# 14. Copy a dictionary into another dictionary. Explain whether changing a
#     nested object in the copy can affect the original.


students = {
    "stu01":{
        "name":"Farhan",
        "age":21,
        "marks":{
            "acc":88,
            "bus":75,
            "tech":56
        }
    },
    "stu02":{
        "name":"ram",
        "age":22,
        "marks":{
            "acc":96,
            "bus":56,
            "tech":80
        }
    }
}
new_var = students
new_var["stu01"]["marks"] = {
            "Machine_learning":88,
            "english":75,
            "AI":56
        }
print(students)

# sourab & Gourav
# print(print())
# print(10 and 20)
# print(10 or 20)


