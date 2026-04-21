import re

def get_student_name():
    while True:
        name = input("Enter student's name: ").strip()
        if name:
            return name
        else:
            print("Invalid input. Name cannot be empty.")

def get_student_id():
    while True:
        student_id = input("Enter student's ID: ").strip()
        if re.fullmatch(r'\d+', student_id):
            return student_id
        else:
            print("Invalid input. Student ID must be numeric.")
 

def get_student_marks():
    while True:
        try:
            marks = int(input("Enter student's marks: "))
            if 0<= marks <= 100:
                return marks
            else:
                print("Invalid input. Marks must be between 0-100.")
        except ValueError:
            print("Invalid input. Please enter a valid input for number.")                         

