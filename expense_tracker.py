import pandas as pd
from datetime import date

FILE_NAME = "expenses.csv"

def add_expense():
    category = input("Enter category (Food/Travel/etc): ")
    amount = float(input("Enter amount: "))
    today = date.today()

    df = pd.read_csv(FILE_NAME)
    new_data = {
        "Date": today,
        "Category": category,
        "Amount": amount
    }

    df = df._append(new_data, ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

    print("Expense added successfully!")

def view_summary():
    df = pd.read_csv(FILE_NAME)
    print("Total Expense:", df["Amount"].sum())
    print("Category-wise Expense:")
    print(df.groupby("Category")["Amount"].sum())

while True:
    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_summary()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
