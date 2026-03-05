

def addstudent():
        name = input("Enter student name")
        marks = input("Enter studednt marks")
        marks = float(marks)
        with open("student.txt", "a") as file:
            lines = file.write(f"{name},{marks}\n")

        print("Student data added")


def viewstudent():
    try:
        with open("student.txt", "r") as file:
             lines = file.readlines()

        if not lines:
            print("No data found")
            return

        for line in lines:
            name, marks = line.strip().split(",")
            print(f"Name: {name}, Marks: {marks}")
    except FileNotFoundError:
         print("No file found")


def searchstudent():
     try:
        search_name = input("Enter student name")
        with open("student.txt", "r") as file:
             lines = file.readlines()

        if not lines:
             print("No student found")
             return

        found = False

        for line in lines:
             name, marks = line.strip().split(",")
             if name.lower() == search_name.lower():
                  print(f"Name: {name}, Marks: {marks}")
                  found = True
                  return

        if not found:
            print("Student not found")

     except FileNotFoundError:
         print("No file found")


def average_marks():
    try:
        with open("student.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No students to calculate average.\n")
            return

        total = 0
        count = 0

        for line in lines:
             student, marks = line.strip().split(",")
             marks = float(marks)
             total += marks
             count += 1

        print("Average marks: ", total / count)

    except FileNotFoundError:
         print("No file found")


def highest_marks():
     try:
        with open("student.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No students to calculate average.\n")
            return

        highest_marks = -1
        topper = ""

        for line in lines:
            student, marks = line.strip().split(",")
            marks = float(marks)
            if marks > highest_marks:
                highest_marks = marks
                topper = student

        print(f"Highest marks: {highest_marks}, Topper: {topper}")

     except FileNotFoundError:
         print("No file found")


while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Average Marks")
        print("5. Highest Marks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addstudent()
        elif choice == "2":
            viewstudent()
        elif choice == "3":
            searchstudent()
        elif choice == "4":
            average_marks()
        elif choice == "5":
            highest_marks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
