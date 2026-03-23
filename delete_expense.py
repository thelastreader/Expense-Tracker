import os
import json


def delete_single_expense(records, person_name):
    """🗑️ Delete individual expense categories for a person."""
    while True:
        category_name = input("📝 Enter expense category to delete (e.g., Food, Travel): ").strip().title()

        if category_name not in records[person_name]:
            print("❌ Invalid expense category.")
            continue_choice = input("🔄 Try again? (y/n): ")
            if continue_choice.lower() != 'y':
                return
            continue

        del records[person_name][category_name]
        print(f"✅ '{category_name}' deleted successfully! 🗑️")

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

        user_choice = input("➕ Delete another expense? (y/n): ")
        if user_choice.lower() == 'n':
            return


def delete_entire_record(records, person_name):
    """💥 Delete all expenses for a person."""
    del records[person_name]
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)
    print("✅ Entire record deleted successfully! 💨")


def delete_expense():  # ✅ KEPT SAME - main function name unchanged
    """📋 Main deletion menu function."""
    if not os.path.exists("data.json"):
        print("❌ Record does not exist.")
        return

    with open("data.json", "r", encoding="utf-8") as file:
        try:
            records = json.load(file)
        except json.decoder.JSONDecodeError:
            print("⚠️ Record is corrupted or empty.")
            return

    person_name = input("👤 Enter your name: ").strip().title()

    if person_name not in records:
        print("❌ Invalid person name.")
        return

    print("🗑️ What would you like to delete?")
    print("1️⃣ Delete an expense")
    print("2️⃣ Delete your entire record")

    try:
        user_choice = int(input("🎯 Enter your choice (1/2): "))
    except ValueError:
        print("❌ Invalid input. Please enter 1 or 2.")
        return

    if user_choice not in (1, 2):
        print("❌ Invalid choice.")
        return

    if user_choice == 1:
        delete_single_expense(records, person_name)
    elif user_choice == 2:
        delete_entire_record(records, person_name)