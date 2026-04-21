import pandas as pd

def calculate_average(students):
    if students:
        df = pd.DataFrame([student.__dict__ for student in students])
        return df['marks'].mean()
    return 0

def calculate_highest_marks(students): 
    if students:    
        df = pd.DataFrame([student.__dict__ for student in students])
        highest_student = df.loc[df['marks'].idxmax()]
        return highest_student['marks'],highest_student['name']
    return None,None

def count_passed_students(students):
    df = pd.DataFrame([student.__dict__ for student in students])
    return len(df[df['marks'] > 60])

def count_failed_students(students):
    df = pd.DataFrame([student.__dict__ for student in students])
    return len(df[df['marks'] < 60])
