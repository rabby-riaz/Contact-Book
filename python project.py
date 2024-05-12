1
def ShowFunction():
    print("Name \t Contact")
    for key, value in Contact.items():
        print(f"{key}\t{value}")

Contact = {}
while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Please enter the number corresponding to your choice: ")

    if choice == "1":
        name = input("Enter the contact name: ")
        phone = input("Enter the contact phone number: ")
        Contact[name] = phone
    elif choice == "2":
        contact_name = input("Enter the contact name to search: ")
        if contact_name in Contact:
            print(f"{contact_name}'s contact number is {Contact[contact_name]}")
        else:
            print("Contact not found.")
    elif choice == "3":
        if not Contact:
            print("No contacts found.")
        else:
            ShowFunction()
    elif choice == "4":
        edit_contact = input("Enter the contact name to edit: ")
        if edit_contact in Contact:
            phone = input("Enter the new contact phone number: ")
            Contact[edit_contact] = phone
            print("Contact updated.")
            ShowFunction()
        else:
            print("Contact not found.")
    elif choice == "5":
        delete_contact = input("Enter the contact name to delete: ")
        if delete_contact in Contact:
            delete_confirm = input("Are you sure you want to delete this contact? (y/n): ")
            if delete_confirm.lower() == "y":
                Contact.pop(delete_contact)
                print("Contact deleted.")
                ShowFunction()
            else:
                print("Deletion canceled.")
        else:
            print("Contact not found.")
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a valid option.")

print("Exiting the contact management system.")
