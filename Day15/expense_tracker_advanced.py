## Expense Tracker (File Based) Program

expenses = []


# Load data
def load_data():
    expenses.clear()
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                expenses.append({
                    "category": category,
                    "amount": float(amount)
                })
    except FileNotFoundError:
        pass


# Save data
def save_data():
    with open("expenses.txt", "w") as file:
        for e in expenses:
            file.write(f"{e['category']},{e['amount']}\n")
    print("Data saved successfully!")


# Add expense
def add_expense():
    category = input("Enter category: ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    expenses.append({"category": category, "amount": amount})
    print("Expense added!")


# View expenses
def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== Expenses =====")
    for e in expenses:
        print("-" * 30)
        print(f"Category : {e['category']}")
        print(f"Amount   : {e['amount']}")
    print("-" * 30)


# Total spending
def total_expense():
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Spending: {total}")


# Highest expense
def highest_expense():
    if not expenses:
        print("No data.")
        return

    highest = max(expenses, key=lambda x: x["amount"])
    print("\nHighest Expense:")
    print(f"Category: {highest['category']}")
    print(f"Amount  : {highest['amount']}")


# Main menu
def main():
    load_data()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Highest Expense")
        print("5. Save Data")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            highest_expense()
        elif choice == "5":
            save_data()
        elif choice == "6":
            save_data()
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
