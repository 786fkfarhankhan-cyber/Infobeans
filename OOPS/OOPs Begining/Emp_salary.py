# 6. Write a Python program to create a class called "Employee" with a name, job title, and salary attributes, and methods to calculate and update salary.

class Emp:
    def __init__(self,name,job,salary):
        self.__name = name
        self.__job = job
        self.__salary = salary
    def set_salary(self,salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def cal_salary(self,total_days):
        working_day = int(input("Enter ur Working Days = "))
        one_day = self.__salary//total_days
        monthly_salary = working_day*one_day
        print(f"Your Salary = {monthly_salary}")
    def details(self):
        print(f"Your Name = {self.__name}")
        print(f"Your Job = {self.__job}")
        print(f"Your Salary = {self.__salary}")



e1 = Emp("Far", "data analyst", 30000)

e1.set_salary(50000)
print()
e1.details()
print()
e1.cal_salary(31)












