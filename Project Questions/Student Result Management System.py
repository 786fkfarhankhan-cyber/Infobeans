# 2. Student Result Management System
# Beginner
# Concepts: Conditions, loops, functions
# Requirements
# •	Input marks for five subjects.
# •	Calculate total, percentage, and grade.
# •	Check whether the student passed or failed.
# •	Validate that each mark is between 0 and 100.
# •	Create functions such as calculate_total(), calculate_percentage(), and calculate_grade().
# Bonus: Accept results for multiple students and calculate the class average.

def calculate_total(m1, m2, m3, m4, m5):
    return m1 + m2 + m3 + m4 + m5
m1 = float(input("Enter marks for English : "))
m2 = float(input("Enter marks for Math : "))
m3 = float(input("Enter marks for Softskill : "))
m4 = float(input("Enter marks for Programming : "))
m5 = float(input("Enter marks for Science : "))

def calculate_percentage(total):
    return (total/500)*100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


if (0 <= m1 <= 100) and (0 <= m2 <= 100) and (0 <= m3 <= 100) and (0 <= m4 <= 100) and (0 <= m5 <= 100):
    total = calculate_total(m1, m2, m3, m4, m5)
    percentage = calculate_percentage(total)
    grade = calculate_grade(percentage)

    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

    if percentage >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")
else:
    print("Invalid marks")







