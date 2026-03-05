class StudentManager:

    def __init__(self, filename):
        self.filename = filename

    def _read_lines(self):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                return lines

        except FileNotFoundError:
            return []

    def add_student(self, student, marks):

        with open(self.filename, "a") as file:
            file.write(f"{student},{marks}\n")

        return "Details added"

    def view_students(self):

        lines = self._read_lines()

        if not lines:
            return []

        students = []
        for line in lines:
            student, marks = line.strip().split(",")
            marks = float(marks)
            students.append((student, marks))

        return students

    def average_marks(self):

        lines = self._read_lines()

        if not lines:
            return None

        total = 0
        count = 0

        for line in lines:
            student, marks = line.strip().split(",")
            total += float(marks)
            count += 1

        return total / count

    def highest_marks(self):

        lines = self._read_lines()

        if not lines:
            return None

        highest = -1
        topper = ""

        for line in lines:
            student, marks = line.strip().split(",")
            marks = float(marks)

            if marks > highest:
                highest = marks
                topper = student

        return (topper, highest)

    def search_student(self, search_name):

        lines = self._read_lines()

        if not lines:
            return None

        for line in lines:
            student, marks = line.strip().split(",")
            if student.lower() == search_name.lower():
                return student, marks

        return None

    def menu(self):
        while True:
            print("1. Add student")
            print("2. View students")
            print("3. Average marks")
            print("4. Highest marks")
            print("5. Search student")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.average_marks()
            elif choice == "4":
                self.highest_marks()
            elif choice == "5":
                self.search_student()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid option.\n")


manager = StudentManager("students.txt")
manager.menu()
