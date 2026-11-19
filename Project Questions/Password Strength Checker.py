

def check_length(password):
    if len(password) >= 8:
        return "yes"
    return "no"


def check_capital(password):
    for letter in password:
        if letter.isupper():
            return "yes"
    return "no"


def check_small(password):
    for letter in password:
        if letter.islower():
            return "yes"
    return "no"


def check_number(password):
    for letter in password:
        if letter.isdigit():
            return "yes"
    return "no"


def check_special(password):
    for letter in password:
        if letter in "@#$%&*!?":
            return "yes"
    return "no"


def count_points(password):
    points = 0
    if check_length(password) == "yes":
        points = points + 1
    if check_capital(password) == "yes":
        points = points + 1
    if check_small(password) == "yes":
        points = points + 1
    if check_number(password) == "yes":
        points = points + 1
    if check_special(password) == "yes":
        points = points + 1
    return points


def get_result(points):
    if points <= 2:
        return "Weak"
    elif points <= 4:
        return "Medium"
    else:
        return "Strong"



def show_suggestions(password):
    print("Ways to improve your password:")
    if check_length(password) == "no":
        print("- Use at least 8 characters")
    if check_capital(password) == "no":
        print("- Add a capital letter (A-Z)")
    if check_small(password) == "no":
        print("- Add a small letter (a-z)")
    if check_number(password) == "no":
        print("- Add a number (0-9)")
    if check_special(password) == "no":
        print("- Add a special character (@ # $ % & * ! ?)")



password = input("Enter password: ")

points = count_points(password)
print("Points:", points, "/ 5")
print("Your password is:", get_result(points))

if points < 5:
    show_suggestions(password)