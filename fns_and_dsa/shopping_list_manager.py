def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()  # Display the menu to the user
        choice = input("Enter your choice: ")

        if choice == '1':  # Add Item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")
        
        elif choice == '2':  # Remove Item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        
        elif choice == '3':  # View List
            if shopping_list:
                print("Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is empty.")
        
        elif choice == '4':  # Exit
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

if __name__ == "__main__":
    main()

