# Employee Record System
# Create a class Employee with private fields: id, name, and salary.
# Use setter methods to assign values. Add a method to display employee details.

print("*"*11,"Employee Record System","*"*11 )
class Employee:
    def __init__(self,id,name,salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def display_emp_detail(self):
        print(f"ID : {self.__id} \nName : {self.__name} \nSalary : {self.__salary}")
  
e1 = Employee(101,"Farhan",40000)
e2 = Employee(102,"Roma",20300)
e3 = Employee(103,"Kran",19000)
e4 = Employee(104,"Ertugrul",30000)

e1.display_emp_detail()
print()
e2.display_emp_detail()
print()
e3.display_emp_detail()
print()
e4.display_emp_detail()








