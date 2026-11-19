class Student:
    __student_count = 0
 
    def __init__(self, roll_no, name, m1, m2, m3):
        self.__roll_no = roll_no
        self.__name = name
        self.__marks = [m1, m2, m3]
        Student.__student_count += 1
 
    def calculate_total(self):
        return sum(self.__marks)
 
    def calculate_percentage(self):
        return self.calculate_total() / 3
 
    def calculate_grade(self):
        per = self.calculate_percentage()
        if per >= 90:
            return "A"
        elif per >= 75:
            return "B"
        elif per >= 50:
            return "C"
        else:
            return "Fail"
 
    def display(self):
        print("Roll Number:", self.__roll_no)
        print("Name:", self.__name)
        print("Total:", self.calculate_total())
        print("Percentage:", self.calculate_percentage())
        print("Grade:", self.calculate_grade())
 
    @classmethod
    def get_student_count(cls):
        return cls.__student_count
 
 
s1 = Student(1, "Farhan", 90, 85, 95)
s1.display()
print()
s2 = Student(2, "Prabhat", 34, 42, 30)
s2.display()
print()
s3 = Student(3, "Laksh", 95, 89, 54)
s3.display()
print()
s4 = Student(4, "Rehan", 50, 82, 30)
s4.display()
print()
s5 = Student(5, "Tanisha", 50, 56, 20)
s5.display()
print()
print("Total students:", Student.get_student_count())

