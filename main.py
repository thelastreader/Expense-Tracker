from add_expense import add_expense  # Import the add_expense function

def main():
    """
    Main menu for expense manager.
    Can be extended to include view and delete functions.
    """
    while True:
        print("===== Expense Manager =====")
        print("1. Add Expense")
        print("2. View Expenses (Coming Soon)")
        print("3. Delete Expense (Coming Soon)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            print("📖 View functionality not implemented yet.\n")
        elif choice == "3":
            print("🗑️ Delete functionality not implemented yet.\n")
        elif choice == "4":
            print("👋 Exiting Expense Manager. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.\n")


if __name__ == "__main__":
    main()