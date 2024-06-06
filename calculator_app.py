# Task 1: Create functions for each arithmetic operation

def addition(a, b):
    print("You have chosen to add: ", a + b)

addition(20, 62)    


def subtraction(a, b):
    print("You have chosen to subtract: ", a - b)

subtraction(125, 87)  


def multiplication(a, b):
    print("You have chosen to multiply: ", a * b)

multiplication(15, 12)    


def division(a, b):
    print("You have chosen to divide: ", round(a / b, 2))

division(885, 42)    


# Task 2: Implement user input to receive numbers and an operation choice

num1 = int(input("Enter a number to perform operation on: "))

num2 = int(input("Enter a second number to perform operation on: "))

operations = input("""Choose the operation you will like to perform: addition, subtraction, multiplication and division:
                   
                   1 - Addition
                   2 - Subtraction
                   3 - Multiplication
                   4 - Diivision
                   5 - Quit
                   """)


if operations == "1":
    addition(num1, num2)
elif operations == "2":
     subtraction(num1, num2)
elif operations == "3":
     multiplication(num1, num2)
elif operations == "4":
    division(num1, num2)
elif operations == "5":
    print("You have chosen to quit, Goodbye")
else:
    print("Choose one of the provided operations")