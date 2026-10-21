# 6. Remove a key from a dictionary using pop(). Handle the case where the
#    key does not exist.

student = {
    "name" : "Farhan" ,
    "age" : 21 ,
    "marks" : [89,75,34,53] ,
    

}
if "city" in student:
    print(student.pop("city"))
else:
    print("Key not found")

print("\n")
print(student)


