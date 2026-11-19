# 1. Smart Calculator
# Beginner
# Concepts: if-elif-else, while, functions
# Requirements
# •	Display a menu for addition, subtraction, multiplication, division, and modulus.
# •	Take two numbers from the user.
# •	Use separate functions for each operation.
# •	Handle division by zero.
# •	Repeat until the user selects Exit.
# Bonus: Add power and floor division operations.


print("*"*23 , "Show Menu" , "*"*23)
def show_display():
    print("1. For Addition")
    print("2. For Subtraction")
    print("3. For Multiplication")
    print("4. For Division")
    print("5. For Modulus")
    print("6. For Floor Division")
    print("7. For Power")
    print("8. For Terminate Program")
show_display()




def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if b == 0:
        print("You trying to divide by zero its wrong")
    return a/b
def modulus(a, b):
    return a % b
def floor_div(a, b):
    if b == 0:
        print("By zero floor division not possible")
    return a//b

def power(a, b):
    return a**b

while True:
    show_display()
    choice = int(input("Enter a Choice (1-8): "))

    a = int(input("Enter a First Numbers = "))
    b = int(input("Enter a Second Numbers = "))
    print(f"First Number is - {a} , \nSecond Number is - {b}")
        
    if choice not in [1,2,3,4,5,6,7,8]:
        print("You Made Wrong Choice try Again Please")
        continue
    elif choice == 1 :
        print("You Choose Addition")
        result = add(a,b)
    elif choice == 2 :
        print("You Choose Substraction")
        result = sub(a,b)
    elif choice == 3 :
        print("You Choose Multiplication")
        result = mul(a,b)
    elif choice == 4 :
        print("You Choose Division")
        result = div(a,b)
    elif choice == 5 :
        print("You Choose Modulus")
        result = modulus(a,b)
    elif choice == 6 :
        print("You Choose Floor Division")
        result = floor_div(a,b)
    elif choice == 7 :
        print("You Choose Power")
        result = power(a,b)
    elif choice == 8 :
        print("You Choose Terminate the Program")
        break

    print(f"Result = {result}")



























