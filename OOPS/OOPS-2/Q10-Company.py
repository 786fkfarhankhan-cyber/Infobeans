class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
 
    def display(self):
        print("Name:", self.name, "Salary:", self.salary)
 
 
class Department:
    def __init__(self, dept_name):
        self.__dept_name = dept_name
        self.__employees = []
 
    def add_employee(self, employee):
        self.__employees.append(employee)
        print("Employee added")
 
    def display_employees(self):
        print("Department:", self.__dept_name)
        for emp in self.__employees:
            emp.display() 
 
    def total_salary(self):
        total = 0
        for emp in self.__employees:
            total += emp.salary
        return total
 
 
e1 = Employee("Rahul", 50000)
e2 = Employee("Aman", 40000)
d1 = Department("IT")
d1.add_employee(e1)
d1.add_employee(e2)
d1.display_employees()
print("Total Department Salary:", d1.total_salary())
