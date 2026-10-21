# 2. Given a dictionary of student details, print each key and value on a
#    separate line.
student = {
    "name" : "Farhan" ,
    "age" : 21 ,
    "marks" : [89,75,34,53]
}
print("\n")
print(student)
print("\n")
for key,value in student.items():
    print(key," : ",value)