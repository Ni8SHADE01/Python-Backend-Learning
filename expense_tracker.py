# create an empty list
expenses = []

# define add expense function


def add_expense():
    amount = float(input("Enter the amount : "))
    category = input("Enter the category : ")
    expenses.append({"amount": amount, "category": category})
    print("Expense added \n")

# define view expense function with condition if no expense added


def view_expense():
    if not expenses:
        print("No expense added\n")
        return

    for exp in expenses:
        print(f"category : {exp['category']}, amount : {exp['amount']}")
    print()


# define total expense function
def total_expense():
    total = 0
    for exp in expenses:
        total += exp['amount']

    print("Total amount", total)


# loop for selecting what to do
while True:
    print("1. Add expense")
    print("2. View expense")
    print("3. Total expense")
    print("4. Exit")
    # giving choice to user
    choice = input("Choose an option")

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
