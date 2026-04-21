from input_handler import get_student_name, get_student_id, get_student_marks
from student import Student
from analyzer import calculate_average, calculate_highest_marks, count_passed_students, count_failed_students
from file_handler import read_students_from_file, write_student_to_file
from visualizer import generate_marks_distribution, generate_grade_distribution

def main():
    students = read_students_from_file('students.csv')

    while True:
        print("\n1. Add Student\n2. View Statistics\n3. View marks distribution\n4. View grades distribution\n5. Overview\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = get_student_name()
            student_id = get_student_id()
            marks = get_student_marks()

            student = Student(student_id, name, marks)
            students.append(student)
            write_student_to_file('students.csv', student)
            print(f"Student {name} added successfully.")

        elif choice == '2':
            avg_marks = calculate_average(students)
            highest_marks, highest_name = calculate_highest_marks(students)
            passed = count_passed_students(students)
            failed = count_failed_students(students)

            print(f"\nAverage Marks: {avg_marks:.2f}")
            print(f"Highest Marks: {highest_marks} by {highest_name}")
            print(f"Passed Students: {passed}")
            print(f"Failed Students: {failed}")

        elif choice == '3':
            generate_marks_distribution(students)
        elif choice == '4':    
            generate_grade_distribution(students)

        elif choice == '5':
            for student in students:
                student.prt()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

