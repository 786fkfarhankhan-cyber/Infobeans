# 9. Write a Python program to create a class called "Employee" with a name, salary, and hire date attributes, and a method to calculate years of service.

class Employee:
    def __init__(self,name,salary,hire_year):
        self.__name = name
        self.__salary = salary
        self.__hire = hire_year
    def calculate_years_service(self,resign_year):
        return resign_year - self.__hire
    def display(self):
        print(f"Name: {self.__name}\nSalary: {self.__salary}\nHire Year: {self.__hire}\nYear of Service: {self.calculate_years_service(resign_year)}") 

resign_year = int(input("Enter a Resign year: ")) 

emp1 = Employee("Atul",85000,2022)
emp2 = Employee("John",20000,2025)
emp1.display()             
print()
emp2.display()











