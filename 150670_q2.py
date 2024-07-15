class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students in the classroom.\n")
        else:
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grades}")
            print()

    def get_student_average(self, student_name):
        for student in self.students:
            if student.name.lower() == student_name.lower():
                return student.get_average_grade()
        return None

    def get_class_average_for_subject(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            return 0
        return total / count

# Demonstrating the functionality
def main():
    classroom = Classroom()

    while True:
        print("1. Add a student")
        print("2. Add grade for a student")
        print("3. Display all students")
        print("4. Get average grade of a student")
        print("5. Get class average for a subject")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            student = Student(name)
            classroom.add_student(student)
            print(f"Student {name} added successfully.\n")
        elif choice == '2':
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            for student in classroom.students:
                if student.name.lower() == name.lower():
                    student.add_grade(subject, grade)
                    print(f"Grade {grade} for {subject} added to student {name}.\n")
                    break
            else:
                print(f"Student {name} not found.\n")
        elif choice == '3':
            classroom.display_students()
        elif choice == '4':
            name = input("Enter student name: ")
            average = classroom.get_student_average(name)
            if average is not None:
                print(f"Average grade for {name} is {average:.2f}\n")
            else:
                print(f"Student {name} not found.\n")
        elif choice == '5':
            subject = input("Enter subject: ")
            average = classroom.get_class_average_for_subject(subject)
            print(f"Class average for {subject} is {average:.2f}\n")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()