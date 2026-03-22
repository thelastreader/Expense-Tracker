import json
import os

def add_expense():
    """
    Adds expense(s) for a given person to the data.json file.
    The structure is: { "PersonName": { "ExpenseType": Amount, ... } }
    """

    # Ask for person's name
    person_name = input("Enter the name of the person: ")

    # Load existing data if JSON file exists
    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as file:
            try:
                data = json.load(file)  # JSON -> Python dict
            except json.JSONDecodeError:
                data = {}  # If file is empty/corrupted
    else:
        data = {}

    # Ensure person entry exists
    if person_name not in data:
        data[person_name] = {}

    # Loop to add multiple expenses
    while True:
        expense_type = input("Enter expense type (e.g., Food, Travel): ")
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")
            continue

        # Add/update expense
        data[person_name][expense_type] = amount

        # Ask if user wants to add more expenses
        more = input("Add another expense? (Y/N): ")
        if more.lower() == "y":
            continue
        elif more.lower() == "n":
            break
        else:
            print("❌ Invalid choice. Exiting add operation.")
            break

    # Save back to JSON
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"\n✅ Expenses for {person_name} saved successfully.\n")