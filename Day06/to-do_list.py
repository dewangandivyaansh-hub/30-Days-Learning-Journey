# To-Do List Program

tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # 1. Add Task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    # 2. Remove Task
    elif choice == "2":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found!")

    # 3. Display Tasks
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    # 4. Exit
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
