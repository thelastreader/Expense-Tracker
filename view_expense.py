import os
import json


def view_expense():
    """
    View expense records for a specific person.
    """
    # Load data safely
    if not os.path.exists("data.json"):
        print("❌ No records file found!")
        return

    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        print("❌ Records file is corrupted or empty!")
        return

    # Get person name
    person_name = input("👤 Enter your name: ").strip().title()

    # Validate person exists
    if person_name not in data:
        print("❌ Person not found in records!")
        return

    # Display expenses with numbering
    person_record = data[person_name]
    print(f"\n✨ {person_name}'s Expense Record ✨")
    print("=" * 40)

    i = 1
    total = 0
    for key, value in person_record.items():
        print(f"{i}. 📊 {key}: ₹{value}")
        total += value
        i += 1

    print("=" * 40)
    print(f"💰 Total Expenses: ₹{total}")
    print("-" * 40)