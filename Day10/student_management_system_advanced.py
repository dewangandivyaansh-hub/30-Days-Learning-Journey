## A file-based Python program to manage student records (add, view, search, update, delete)-

students = []

# Load data from file
def load_data():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll, marks = line.strip().split(",")
                students.append({"name": name, "roll": roll, "marks": marks})
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
    roll = input("Enter roll number: ")

    # check duplicate roll
    for s in students:
        if s["roll"] == roll:
            print("Roll number already exists!")
            return

    name = input("Enter name: ")
    marks = input("Enter marks: ")

    students.append({"name": name, "roll": roll, "marks": marks})
    print("Student added successfully!")


# View students
def view_data():
    if not students:
        print("No records found.")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"Name: {s['name']} | Roll: {s['roll']} | Marks: {s['marks']}")


# Search student
def search_data():
    roll = input("Enter roll number: ")

    for s in students:
        if s["roll"] == roll:
            print(f"Found -> Name: {s['name']}, Marks: {s['marks']}")
            return

    print("Student not found.")


# Delete student
def delete_data():
    roll = input("Enter roll number to delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted!")
            return

    print("Student not found.")


# Update student
def update_data():
    roll = input("Enter roll number to update: ")

    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")
            s["marks"] = input("Enter new marks: ")
            print("Student updated!")
            return

    print("Student not found.")


# Main menu
def main():
    load_data()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_data()
        elif choice == "2":
            view_data()
        elif choice == "3":
            search_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            update_data()
        elif choice == "6":
            save_data()
        elif choice == "7":
            save_data()
            print("Exiting program...")
            break
        else:
            print("Invalid choice")
