expenses = {
    "Rent": 15000,
    "Food": 6000,
    "Travel": 3500,
    "Bills": 2800
}

total = sum(expenses.values())
highest = max(expenses, key=expenses.get)

print("Monthly Expense:", total)
print("Highest Category:", highest)

for category, amount in expenses.items():
    print(category, ":", amount)
