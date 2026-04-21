import pandas as pd
from student import Student

def read_students_from_file(filename):
    students = []
    try:
        df=pd.read_csv(filename)
        for i,j in df.iterrows():
            marks = int(j['marks']) if not isinstance(j['marks'], int) else j['marks']
            student = Student(j['student_id'],j['name'],marks)
            students.append(student)
    except FileNotFoundError:
        print("File not found. Making new list.")
    return students

def write_student_to_file(filename, student):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["student_id","name","marks"])

    new_student = pd.DataFrame([[student.student_id, student.name, student.marks]], columns=['student_id','name','marks'])    
    df = pd.concat([df, new_student], ignore_index=True)

    df.to_csv(filename, index=False)





    