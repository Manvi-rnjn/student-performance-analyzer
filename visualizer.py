import matplotlib.pyplot as plt
import pandas as pd

def generate_marks_distribution(students):
    df = pd.DataFrame([student.__dict__ for student in students])
    plt.hist(df['marks'], bins=10, edgecolor='black')
    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.show()

def generate_grade_distribution(students):
    df = pd.DataFrame([student.__dict__ for student in students])
    grade_counts = df['grade'].value_counts()
    
    plt.bar(grade_counts.index, grade_counts.values, color = "purple", edgecolor = "black")
    plt.title("Grade Distribution")
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.show()

