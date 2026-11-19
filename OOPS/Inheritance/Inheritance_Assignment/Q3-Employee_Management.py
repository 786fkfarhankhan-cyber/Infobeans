# 3. Employee Management

# Base class Employee.

# Derived:

# Developer
# Tester
# HR

# Calculate salaries differently.
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def cal_salary(self,role,salary):
        # income_tax = float(input("Enter Income Tax Rate = "))
        # total_salary = salary - (income_tax/100*100)
        # print(total_salary)
        pass


class Developer(Employee):
    def cal_salary(self,role,salary):
        self.__role = role
        self.__salary = salary
        income_tax = float(input("Enter Income Tax Rate = "))
        total_salary = self.__salary - (self.__salary*(income_tax/100))
        print(f"For Role - {self.__role}")
        print(f"Salary Before Tax - {self.__salary}")
        print(f"Income Tax Rate - {income_tax}")
        print(f"The Salary of Developer - {total_salary}")

class Tester(Employee):
    def cal_salary(self,role,salary):
        self.__role = role
        self.__salary = salary
        income_tax = float(input("Enter Income Tax Rate = "))
        total_salary = self.__salary - (self.__salary*(income_tax/100))
        print(f"For Role - {self.__role}")
        print(f"Salary Before Tax - {self.__salary}")
        print(f"Income Tax Rate - {income_tax}")
        print(f"The Salary of Tester - {total_salary}")


class Hr(Employee):
    def cal_salary(self,role,salary):
        self.__role = role
        self.__salary = salary
        income_tax = float(input("Enter Income Tax Rate = "))
        total_salary = self.__salary - (self.__salary*(income_tax/100))
        print(f"For Role - {self.__role}")
        print(f"Salary Before Tax - {self.__salary}")
        print(f"Income Tax Rate - {income_tax}")
        print(f"The Salary of HR - {total_salary}")

dev = Developer()
dev.cal_salary("Developer",50000)
print()
test = Tester()
test.cal_salary("Software",90000)
print()
hr = Hr()
hr.cal_salary("Hu",83383)