# Contact Book using File Handling

FILE_NAME = "contacts.txt"

# Load contacts from file
def load_contacts():
    contacts = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

# Add new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone
    save_contacts(contacts)
    print("Contact added successfully!")

# Search contact
def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}")
    else:
        print("Contact not found!")

# Main menu
def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Show All Contacts")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            for name, phone in contacts.items():
                print(name, "-", phone)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

# Run program
main()# Contact Book using File Handling

FILE_NAME = "contacts.txt"

# Load contacts from file
def load_contacts():
    contacts = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

# Add new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone
    save_contacts(contacts)
    print("Contact added successfully!")

# Search contact
def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}")
    else:
        print("Contact not found!")

# Main menu
def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Show All Contacts")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            for name, phone in contacts.items():
                print(name, "-", phone)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

# Run program
main()
