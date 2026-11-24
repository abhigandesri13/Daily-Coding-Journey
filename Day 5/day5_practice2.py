# Level 3 – Practical mini project

# Mini project – Shopping List Manager

'''Practical application
Now let's combine lists, loops and conditional statements from your previous lessons.

Requirements:
- Start with an empty shopping list.
- Add an item.
- Remove an item.
- Display all items.
- Show the total number of items.
- Exit the program. '''

shopping_list = []

while True:

    print("\n--- Shopping List Manager ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display items")
    print("4. Total items")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        shopping_list.append(item)
        print("\nItem added successfully.")

    elif choice == "2":
        if len(shopping_list) == 0:
            print("\nYour shopping list is empty.")
        else:
            item = input("Enter item to remove: ")
            if item in shopping_list:
               shopping_list.remove(item)
               print("\nItem removed successfully.")
            else:
               print("\nItem not found.")

    elif choice == "3":
        if len(shopping_list) == 0:
            print("\nYour shopping list is empty.")
        else:
            print("\nYour shopping list:", shopping_list)

    elif choice == "4":
        print("\nTotal items:", len(shopping_list))

    elif choice == "5":
        print("\nThank you!")
        break

    else:
        print("\nInvalid choice. Please try again.")