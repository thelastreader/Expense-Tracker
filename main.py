from add_expense import add_expense  # Import the add_expense function
from view_expense import view_expense  # Import the view_expense function
from delete_expense import delete_expense  # Import the delete_expense function

def main():
    """
    Main menu for expense manager.
    Can be extended to include view and delete functions.
    """
    while True:

        print("      🎯 EXPENSE MANAGER 🎯")

        print("1. ➕ Add Expense")
        print("2. 📊 View Expenses")
        print("3. 🗑️  Delete Expense")
        print("4. 🚪 Exit")


        choice = input("✨ Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("👋 Exiting Expense Manager. Thank you! ✨")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.\n")


if __name__ == "__main__":
    main()