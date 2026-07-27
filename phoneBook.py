phone_book = {}

while True:
    print("\n===== PHONE BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")

        phone_book[name] = number
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter contact name to search: ")

        if name in phone_book:
            print("Name:", name)
            print("Phone Number:", phone_book.get(name))
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter contact name to delete: ")

        if name in phone_book:
            phone_book.pop(name)
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "4":
        if len(phone_book) == 0:
            print("Phone book is empty.")
        else:
            print("\n----- Contact List -----")
            for name, number in phone_book.items():
                print("Name:", name, "| Phone Number:", number)

    elif choice == "5":
        print("Exiting Phone Book...")
        break

    else:
        print("Invalid choice! Please try again.")
