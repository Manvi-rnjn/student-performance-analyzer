class Student:
    def __init__(self,student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'
             
    def prt(self):
        print(f"Student ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}, Grade: {self.grade}")
