## To-Do list Program (File Version)

tasks = []

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a new task
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks()
    print("Task added!")

# View all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Delete a task
def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks()
        print(f"Deleted: {removed}")
    except:
        print("Invalid input.")

# Main program
def main():
    load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# Run program
main()
