## Student management system v2 with improved program

students = []


# Load data from file
def load_data():
    students.clear()
    try:
        with open("students.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, roll, marks = parts
                    students.append({
                        "name": name,
                        "roll": roll,
                        "marks": int(marks)
                    })
    except FileNotFoundError:
        pass


# Save data to file
def save_data():
    with open("students.txt", "w") as file:
        for s in students:
            file.write(f"{s['name']},{s['roll']},{s['marks']}\n")
    print("Data saved successfully!")


# Add student
def add_data():
    roll = input("Enter roll number: ").strip()

    if not roll:
        print("Roll number cannot be empty!")
        return

    for s in students:
        if s["roll"] == roll:
            print("Roll already exists!")
            return

    name = input("Enter name: ").strip()

    try:
        marks = int(input("Enter marks: "))
    except ValueError:
        print("Marks must be a number!")
        return

    students.append({"name": name, "roll": roll, "marks": marks})
    print("Student added successfully!")


# View students
def view_data():
    if not students:
        print("No records found.")
        return

    print("\n===== Student Records =====")
    for s in students:
        print("-" * 30)
        print(f"Name  : {s['name']}")
        print(f"Roll  : {s['roll']}")
        print(f"Marks : {s['marks']}")
    print("-" * 30)


# Search by roll
def search_by_roll():
    roll = input("Enter roll number: ")

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found:")
            print("-" * 30)
            print(f"Name  : {s['name']}")
            print(f"Roll  : {s['roll']}")
            print(f"Marks : {s['marks']}")
            print("-" * 30)
            return

    print("Student not found.")


# Search by name
def search_by_name():
    name = input("Enter name: ").lower()

    found = False
    for s in students:
        if s["name"].lower() == name:
            print("-" * 30)
            print(f"Name  : {s['name']}")
            print(f"Roll  : {s['roll']}")
            print(f"Marks : {s['marks']}")
            print("-" * 30)
            found = True

    if not found:
        print("Student not found.")


# Delete student
def delete_data():
    roll = input("Enter roll number to delete: ")

    for s in students:
        if s["roll"] == roll:
            confirm = input("Are you sure? (yes/no): ").lower()
            if confirm == "yes":
                students.remove(s)
                print("Student deleted!")
            else:
                print("Cancelled.")
            return

    print("Student not found.")


# Update student
def update_data():
    roll = input("Enter roll number to update: ")

    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")

            try:
                s["marks"] = int(input("Enter new marks: "))
            except ValueError:
                print("Marks must be a number!")
                return

            print("Student updated!")
            return

    print("Student not found.")


# Sort students
def sort_students():
    print("1. Sort by Name")
    print("2. Sort by Marks")

    choice = input("Enter choice: ")

    if choice == "1":
        students.sort(key=lambda x: x["name"].lower())
        print("Sorted by name.")
    elif choice == "2":
        students.sort(key=lambda x: x["marks"])
        print("Sorted by marks.")
    else:
        print("Invalid choice.")


# Main menu
def main():
    load_data()

    while True:
        print("\n===== Student Management System v2 =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search by Roll")
        print("4. Search by Name")
        print("5. Delete Student")
        print("6. Update Student")
        print("7. Sort Students")
        print("8. Save Data")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_data()
        elif choice == "2":
            view_data()
        elif choice == "3":
            search_by_roll()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            update_data()
        elif choice == "7":
            sort_students()
        elif choice == "8":
            save_data()
        elif choice == "9":
            save_data()
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
