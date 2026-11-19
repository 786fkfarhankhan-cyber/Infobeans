class Exam:
    __exam_count = 0
 
    def __init__(self, exam_name, total_marks, passing_marks):
        self.__exam_name = exam_name
        self.__total_marks = total_marks
        self.__passing_marks = passing_marks
        Exam.__exam_count += 1
 
    def check_result(self, obtained):
        if 0 <= obtained <= self.__total_marks:
            if obtained >= self.__passing_marks:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Invalid marks")
 
    def calculate_grade(self, obtained):
        if obtained < self.__passing_marks:
            return "F"
        elif obtained >= 90:
            return "A"
        elif obtained >= 75:
            return "B"
        else:
            return "C"
 
    @classmethod
    def get_exam_count(cls):
        return cls.__exam_count
 
 
e1 = Exam("Python", 100, 35)
e1.check_result(80)
print("Grade:", e1.calculate_grade(80))
print("Total exams:", Exam.get_exam_count())
