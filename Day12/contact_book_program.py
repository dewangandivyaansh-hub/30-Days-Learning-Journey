## Contact Book Program

contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

# To add contacts in the contact book
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print("Contact added!")

# To view all contacts added so far in the contact book
    elif choice == "2":
        if contacts:
            for name, phone in contacts.items():
                print(name, ":", phone)
        else:
            print("No contacts found")

# To find a contact from the contact book
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Not found")

 # To update a contact from the contact book
    elif choice == "4":
        name = input("Enter name to update: ")
        if name in contacts:
            contacts[name] = input("Enter new number: ")
            print("Updated!")
        else:
            print("Not found")

# To delete a contact from the contact book
    elif choice == "5":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Deleted!")
        else:
            print("Not found")

# To end the program
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
