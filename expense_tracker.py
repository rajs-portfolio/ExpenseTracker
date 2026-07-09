FILE_NAME = "expenses.txt"

expenses = []

try:
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, amount = line.strip().split(",")
            expenses.append((name, float(amount)))
except FileNotFoundError:
    pass


def save():
    with open(FILE_NAME, "w") as file:
        for name, amount in expenses:
            file.write(f"{name},{amount}\n")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Expense Name: ")
        amount = float(input("Amount: ₹"))

        expenses.append((item, amount))
        save()

        print("Expense Added!")

    elif choice == "2":

        if not expenses:
            print("No expenses found.")

        else:
            print("\nExpenses:")
            for name, amount in expenses:
                print(f"{name} - ₹{amount}")

    elif choice == "3":

        total = sum(amount for _, amount in expenses)
        print(f"\nTotal Expense: ₹{total}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

