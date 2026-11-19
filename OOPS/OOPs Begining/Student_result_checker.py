# Student Result Checker
# Create a class Student with fields: name, mathMarks, scienceMarks.
# Use setters to assign values. Add a method getAverage().


class Result_checker:
    def __init__(self):
        self.__name = None
        self.__math_marks = None
        self.__science_marks = None
    def set_name(self,name):
        self.__name = name
    def set_math_marks(self,math_marks):
        self.__math_marks = math_marks
    def set_science_marks(self,science_marks):
        self.__science_marks = science_marks
    def get_avg(self):
        total = self.__math_marks + self.__science_marks
        avg = total/2
        return avg
    def result_detail(self):
        print(f"Name of The Student : {self.__name}")
        print(f"Math Marks of Student : {self.__math_marks}")
        print(f"Science Marks of Student : {self.__science_marks}")
        print(f"Average marks of Student : {self.get_avg()}")

print("Welcome To Student Result Checker")
s1 = Result_checker()
s1.set_name("fer")
s1.set_math_marks(80)
s1.set_science_marks(80)
s1.get_avg()
s1.result_detail()








