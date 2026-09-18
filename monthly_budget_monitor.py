budget = 50000

expenses = {
    "Rent": 18000,
    "Food": 7000,
    "Travel": 5000,
    "Shopping": 8500
}

spent = sum(expenses.values())
remaining = budget - spent

print("Budget:", budget)
print("Spent:", spent)
print("Remaining:", remaining)

if remaining < budget * 0.2:
    print("Budget Warning")
