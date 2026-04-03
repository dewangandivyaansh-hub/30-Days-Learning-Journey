## Student Management System 

students = {}

# Function to add student
def add_student():
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks separated by space: ").split()))
    students[name] = marks
    print(f"{name} added successfully! \n")

# Function to calculate average marks
def calculate_average():
    name = input("Enter student name: ")
    if name in students:
        avg = sum(students[name]) / len(students[name])
        print(f"Average marks of {name}: {avg:.2f} \n")
    else:
        print("Student not found! \n")

# Function to display all students
def display_students():
    if not students:
        print("No student records found! \n")
        return
    
    for name, marks in students.items():
        print(f"Name: {name}, Marks: {marks}")
    print()

# Main menu
while True:
    print("----- Student Management System -----")
    print("1. Add Student")
    print("2. Calculate Average")
    print("3. Display All Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        calculate_average()
    elif choice == '3':
        display_students()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again. \n")
