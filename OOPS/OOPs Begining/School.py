# 14. Write a Python program to create a class called "School" with attributes for students, teachers, and classes, and methods to add and remove students and teachers, and to create classes.

class School:
    def __init__(self,student,teacher,classes):
        self.__student = student
        self.__teacher = teacher
        self.__classes = classes
    def add_student(self, student):
        self.__student.append(student)

    def remove_student(self, student):
        if student in self.__student:
            self.__student.remove(student)
            print("Student Removed")
        else:
            print("Student Not Found")

    def add_teacher(self,teacher):
        self.__teacher.append(teacher)

    def remove_teacher(self,teacher):
        if teacher in self.__teacher:
            self.__teacher.remove(teacher)
            print("Teacher Remove")
        else:
            print("Teacher not found")
    def create_class(self, class_name):
        self.__classes.append(class_name)
    def detail(self):
        print("Students:", ", ".join(self.__student))
        print("Teachers:", ", ".join(self.__teacher))
        print("Classes:", ", ".join(self.__classes))


# student = []
# teacher = []
# classes = []
s1 = School([], [], [])
s2 = School([], [], [])
s3 = School([], [], [])

# s1 = School("Farhan","meg","Python")
# s2 = School("Arhan","son","Java")
# s3 = School("Ali","zwi","Word")

s1.add_student("Farhan")
s2.add_student("Arhan")
s3.add_student("ali")

s1.add_teacher("mil")
s2.add_teacher("del")
s3.add_teacher("lin")

s1.create_class("Python")
s2.create_class("java")
s3.create_class("mum")

School = [s1, s2, s3]

print("Before Removing student:")
for students in School:
    students.detail()
    print()
s2.remove_student("Arhan")
print()
print("After Removing:")
for students in School:
    students.detail()
    print()

print("Before Removing Teacher:")
for teachers in School:
    teachers.detail()
    print()
s1.remove_teacher("mil")
print()
print("After Removing:")
for teachers in School:
    teachers.detail()
    print()


s1.detail()
print()
s2.detail()
print()
s3.detail()





