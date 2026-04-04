# Student Record System (File Based)

# Add new student
def add_student():
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as file:
        file.write(name + "," + marks + "\n")

    print("Student record added!")

# View all student records
def view_students():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

            if not records:
                print("No records found.")
            else:
                print("\n--- Student Records ---")
                for i, record in enumerate(records, start=1):
                    name, marks = record.strip().split(",")
                    print(f"{i}. Name: {name} | Marks: {marks}")

    except FileNotFoundError:
        print("No records file found.")

# Main menu
def main():
    while True:
        print("\n--- STUDENT RECORD SYSTEM ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# Run program
main()
