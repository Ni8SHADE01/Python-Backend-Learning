# create an empty list
expenses = []

# define add expense function


def add_expense():
    amount = float(input("Enter the amount : "))
    category = input("Enter the category : ")
    expenses.append({"amount": amount, "category": category})

    with open("expenses.txt", "a") as file:
        file.write(f"{category},{amount}\n")

    print("Expense added \n")

# define view expense function with condition if no expense added


def view_expense():

    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No expense added\n")
            return

        for line in lines:
            category, amount = line.strip().split(",")
            amount = float(amount)
            print(f"Category : {category}, Amount : {amount}")

        print()
    except FileNotFoundError:
        print("No expense file found")


# define total expense function
def total_expense():
    total = 0
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            category, amount = line.strip().split(",")
            amount = float(amount)
            total += amount

        print("Total amount", total)

    except FileNotFoundError:
        print("No expense file found")


# loop for selecting what to do
while True:
    print("1. Add expense")
    print("2. View expense")
    print("3. Total expense")
    print("4. Exit")
    # giving choice to user
    choice = input("Choose an option : ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Exiting")
        break
    else:
        print("Invalid choice \n")
