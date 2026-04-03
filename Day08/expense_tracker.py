## Expense Tracker

expenses = []

# Add expense
def add_expense():
    amount = float(input("Enter expense amount: "))
    expenses.append(amount)
    print("Expense added! \n")

# Show total expense
def show_total():
    if not expenses:
        print("No expenses yet! \n")
        return
    print(f"Total Expense: {sum(expenses)} \n")

# Show highest expense
def show_highest():
    if not expenses:
        print("No expenses yet! \n")
        return
    print(f"Highest Expense: {max(expenses)} \n")

# Main menu
while True:
    print("----- Expense Tracker -----")
    print("1. Add Expense")
    print("2. Show Total")
    print("3. Show Highest Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        show_total()
    elif choice == '3':
        show_highest()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice! \n")
