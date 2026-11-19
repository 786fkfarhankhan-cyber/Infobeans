# 4. Student Management
# Base class Person.

# Derived:
# Student
# Teacher

# Add role-specific methods.


from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @abstractmethod
    def subject(self):
        pass

    @abstractmethod
    def attendance(self, percentage):
        pass


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def subject(self):
        print("Which Subject Do You Want To Study?")
        print("1. English")
        print("2. Math")
        print("3. Science")

        ch = int(input("Enter Your Choice: "))

        if ch == 1:
            print("You Chose English")
        elif ch == 2:
            print("You Chose Math")
        elif ch == 3:
            print("You Chose Science")
        else:
            print("Invalid Choice")

    def attendance(self, percentage):
        if percentage < 75:
            print("75% Attendance is Mandatory.")
            print("Your attendance is low.")
        else:
            print("You Fulfill the 75% Attendance Criteria.")


class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.__teacher_id =teacher_id
        

    def subject(self):
        subject = input("Enter Subject You Teach: ")
        print(f"You Teach {subject}.")

    def attendance(self, percentage):
        print("Taking Students Attendance...")
        print(f"Today's Student Attendance: {percentage}%")


stu = Student("far",22,121)
stu.subject()
stu.attendance(60)
print()
tea = Teacher("Sabo",67,102)
tea.subject()
tea.attendance(85)
