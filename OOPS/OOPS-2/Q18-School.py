# 18. School Classroom System
# Problem

# Create classroom system.

# Requirements

# Classroom should:

# maintain student objects
# maintain class teacher
# Functionalities
# Add student
# Remove student
# Display class strength
# Concepts Practiced
# object aggregation
# collections of objects




class Classroom:
    def __init__(self, class_name, teacher):
        self.__class_name = class_name
        self.__teacher = teacher
        self.__students = []

    def add_student(self, student):
        if student not in self.__students:
            self.__students.append(student)
            print(student, "added successfully.")
        else:
            print("Student already exists.")

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)
            print(student, "removed successfully.")
        else:
            print("Student not found.")

    def display_strength(self):
        print("Class Name:", self.__class_name)
        print("Class Teacher:", self.__teacher)
        print("Class Strength:", len(self.__students))

    def display_students(self):
        print("Students in", self.__class_name, "class:")
        for student in self.__students:
            print(student)



c1 = Classroom("Python", "Milan")
c2 = Classroom("Java", "Deepak")
c3 = Classroom("Data Science", "Rahul")


c1.add_student("Farhan")
c1.add_student("Arhan")
c1.add_student("Ali")

c2.add_student("Kapil")
c2.add_student("Vish")

c3.add_student("Mahi")
c3.add_student("Nur")

print("\n--- Before Removing Student ---")

classrooms = [c1, c2, c3]

for classroom in classrooms:
    classroom.display_strength()
    classroom.display_students()
    print()


c1.remove_student("Farhan")

print("\n--- After Removing Student ---")

for classroom in classrooms:
    classroom.display_strength()
    classroom.display_students()
    print()

