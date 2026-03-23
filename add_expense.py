import json
import os


def add_expense():
    """
    Adds/updates expense(s) for a given person to the data.json file.
    Supports negative amounts to reduce expenses (e.g., -50 to deduct ₹50).
    """
    # 👤 Get person details
    person_name = input("👤 Enter person name: ").strip().title()

    # 📂 Load existing data safely
    if os.path.exists("data.json"):
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("⚠️  Corrupted file. Starting fresh...")
            data = {}
    else:
        print("📄 Creating new records file...")
        data = {}

    # Ensure person record exists
    if person_name not in data:
        data[person_name] = {}
        print(f"✨ Created new record for {person_name}")

    print("💡 Amount can't be below ₹0\n")
    print("\n💡 TIP: Use NEGATIVE amounts to REDUCE expenses (e.g., -50)")

    total_change = 0

    # ➕ Add/Update multiple expenses
    while True:
        expense_type = input("📊 Expense type (Food, Travel, etc.): ").strip().title()

        try:
            amount = float(input("💰 Enter amount (₹): "))
        except ValueError:
            print("❌ Invalid amount! Enter a number (e.g., 50 or -25).")
            continue

        # Validate: cannot go below 0
        new_amount = data[person_name].get(expense_type, 0) + amount
        if new_amount < 0:
            print(f"❌ Cannot reduce below ₹0! Current: ₹{data[person_name].get(expense_type, 0)}")
            continue

        # Update expense
        data[person_name][expense_type] = new_amount

        if amount > 0:
            print(f"📈 {expense_type}: +₹{amount} (New: ₹{new_amount})")
        else:
            print(f"📉 {expense_type}: ₹{amount} (New: ₹{new_amount})")

        total_change += amount

        # Continue?
        more = input("➕ Add another? [Y/n]: ").strip().lower()
        if more in ("n", "no"):
            break

    # 💾 Save to file
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"\n🎉 Update complete!")
    print(f"📊 Net change for {person_name}: ₹{total_change:+.2f}")
    print("✨ Records updated successfully!\n")