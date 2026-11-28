# Level 3 – Practical mini project

''' 8. Build a Contact Book using a dictionary.

Requirements:
- Add a contact with name and phone number.
- Search for a contact.
- Update a phone number.
- Delete a contact.
- Display all contacts.
- Exit the program.
Use dictionaries, loops and conditional statements. '''

print("Contact Book")
contact_book = {}

while True:
    
    print("\nChoose an option:  \n 1. Add a contact with name and phone number.\n 2. Search for a contact.\n 3. Update a phone number.\n 4. Delete a contact.\n 5. Display all contacts.\n 6. Exit the program.")
    option = input("\nEnter your option: ")

    if option == "1": 
        name = input("Enter the name: ").strip()
        number = input("Enter the number: ")
        contact_book[name] = number
        print("Successful Added")

    elif option == "2":
        if len(contact_book) == 0:
            print("No contacts")
        else:
            person = input("Name of the contact: ").strip()
            if person in contact_book:
                print("contact found")
                print("number: ",contact_book[person])
            else:
                print("contact not found")

    elif option == "3":
        name = input("Enter contact Name: ").strip()
        if  name in contact_book:
            number = input("Enter updated number: ").strip()
            contact_book[name] = number
            print("contact updated successfully.")
        else:
               print("contact not found.")

    elif option == "4":
        name = input("Enter contact name: ").strip()
        if name in contact_book:
            del contact_book[name]
            print("contact deleted successful.")
        else:
            print("contact not found.")
        
    elif option == "5": 
        if len(contact_book) == 0:
            print("contact book is empty")
        else:
            print(contact_book)

    elif option == "6":
        print("Thank you!")
        break
        
    else:
        print("Invalid choice.")