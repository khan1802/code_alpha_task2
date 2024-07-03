class StudentGradeTracker:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self, subject):
        if subject in self.grades:
            return sum(self.grades[subject]) / len(self.grades[subject])
        else:
            return 0

    def display_grades(self):
        for subject, grades in self.grades.items():
            average = self.calculate_average(subject)
            print(f"Subject: {subject}, Grades: {grades}, Average: {average:.2f}")


def main():
    name = input("Enter student name: ")
    tracker = StudentGradeTracker(name)

    while True:
        print("\n1. Add grade")
        print("2. Display grades")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            tracker.add_grade(subject, grade)
        elif choice == "2":
            tracker.display_grades()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()