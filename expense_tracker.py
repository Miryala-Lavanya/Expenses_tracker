import csv
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

FILENAME = 'expenses.csv'

# Ensure CSV has headers
def init_csv():
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount'])
    except FileExistsError:
        pass

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Rent, Travel): ")
    amount = float(input("Enter amount: "))

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("Expense added successfully.\n")

def show_monthly_totals():
    totals = defaultdict(float)

    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            month = datetime.strptime(row['Date'], '%Y-%m-%d').strftime('%Y-%m')
            key = f"{month} - {row['Category']}"
            totals[key] += float(row['Amount'])

    print("\nMonthly Totals by Category:")
    for key, total in totals.items():
        print(f"{key}: ₹{total:.2f}")
    print()

def plot_charts():
    category_totals = defaultdict(float)

    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category_totals[row['Category']] += float(row['Amount'])

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    # Bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(categories, amounts, color='skyblue')
    plt.title('Expenses by Category - Bar Chart')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.tight_layout()
    plt.show()

    # Pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category - Pie Chart')
    plt.tight_layout()
    plt.show()

def menu():
    init_csv()
    while True:
        print("----- Expense Tracker CLI -----")
        print("1. Add Expense")
        print("2. Show Monthly Totals")
        print("3. Plot Charts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_monthly_totals()
        elif choice == '3':
            plot_charts()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
