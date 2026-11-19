# 10. Write a python program to create a class called "Student" with a name, grade, and courses attributes, and methods to add and remove courses.

class Student_course:
    def __init__(self,name,grade,course):
        self.__name = name
        self.__grade = grade
        self.__course = course
    
    def add_course(self, courses):
        self.__course.append(courses)

    def remove_course(self, courses):
        if courses in self.__course:
            self.__course.remove(courses)
        else:
            print(f"{courses} is not available.")

    def display(self):
        print(f"Name: {self.__name}")
        print(f"Grade: {self.__grade}")
        print(f"Courses: {self.__course}")


stud1 = Student_course("Farhan Khan", "A", ["B.com"])
stud1.add_course("Python")
stud1.add_course("SQL")
print("Student Details:")
stud1.display()
print()


stud2 = Student_course("Love Kasturi", "B", ["MBA"])
stud2.add_course("Communication")
stud2.add_course("Business Studies")
print("Student Details:")
stud2.display()


stud1.remove_course("SQL")
print("\nAfter removing course:")
stud1.display()








