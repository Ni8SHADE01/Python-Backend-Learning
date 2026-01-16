def add_student():
    student = input("Enter student name : ")
    marks = float(input("Enter student marks : "))

    with open("students.txt", "a") as file:
        file.write(f"{student},{marks}\n")

    print("Name and marks added\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No students found.\n")
            return

        for line in lines:
            student, marks = line.strip().split(",")
            marks = float(marks)
            print(f"Name : {student}, Marks : {marks}")

    except FileNotFoundError:
        print("No file found.\n")


def average_marks():
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("Cannot calculate average — no students.\n")
            return

        total = 0
        count = 0

        for line in lines:
            student, marks = line.strip().split(",")
            total += float(marks)
            count += 1

        print("Average marks :", total / count, "\n")

    except FileNotFoundError:
        print("No student data.\n")


def highest_marks():
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No students to check.\n")
            return

        highest = -1
        topper = ""

        for line in lines:
            student, marks = line.strip().split(",")
            marks = float(marks)

            if marks > highest:
                highest = marks
                topper = student

        print(f"Highest marks is {highest}, and topper is {topper}\n")

    except FileNotFoundError:
        print("No student file found.\n")


def search_student():
    search_name = input("Enter student name : ")

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No students to search.\n")
            return

        found = False

        for line in lines:
            student, marks = line.strip().split(",")
            if student.lower() == search_name.lower():
                print(f"Found! Student name : {student}, Marks : {marks}\n")
                found = True
                break

        if not found:
            print("Student not found.\n")

    except FileNotFoundError:
        print("No student file found.\n")


# menu loop
while True:
    print("1. Add student")
    print("2. View students")
    print("3. Average marks")
    print("4. Highest marks")
    print("5. Search student")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        average_marks()
    elif choice == "4":
        highest_marks()
    elif choice == "5":
        search_student()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid option.\n")
