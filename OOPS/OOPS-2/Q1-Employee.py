# Create an Employee class to manage employee details.

# Requirements

# Each employee should have:

# employee id
# name
# department
# salary
# Functionalities
# Display employee details
# Increase salary by percentage
# Count total employees created using a class variable

# Create employee object from a string:

# "101-Rahul-IT-50000"

# using a class method.

# Concepts Practiced
# constructor
# instance variables
# class variables
# class method
# instance methods



class Employee:
    __counter = 0

    def __init__(self, id, name, dept, salary):
        self.__id = id
        self.__name = name
        self.__dept = dept
        self.__salary = salary

        Employee.__counter += 1

    # Display employee details
    def display(self):
        print(f"ID: {self.__id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__dept}")
        print(f"Salary: ₹{self.__salary}")

    # Increase salary by percentage
    def increase_salary(self, per):
        if per > 0:
            self.__salary = self.__salary + (self.__salary * per / 100)
            print("Salary increased successfully!")
            return self.__salary
        else:
            print("Invalid percentage")

    # Create object from string
    @classmethod
    def from_employee(cls, emp_details):
        id, name, dept, salary = emp_details.split("-")

        return cls(int(id), name, dept, float(salary))

    # Get total employee count
    @classmethod
    def get_counter(cls):
        return cls.__counter



emp1 = Employee.from_employee("101-Karl-IT-60000")

print("----- Employee 1 -----")
emp1.display()
emp1.increase_salary(10)

print("\n----- Updated Employee 1 -----")
emp1.display()


print()


emp2 = Employee.from_employee("102-Aman-HR-40000")

print("\n----- Employee 2 -----")
emp2.display()
emp2.increase_salary(10)

print("\n----- Updated Employee 2 -----")
emp2.display()



print("\nTotal Employees:", Employee.get_counter())


