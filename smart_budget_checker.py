income = float(input("Monthly income: "))
expenses = float(input("Monthly expenses: "))

savings = income - expenses

print("Savings:", savings)

if savings > 10000:
    print("Healthy budget ")
elif savings > 0:
    print("Manage spending carefully ")
else:
    print("Overspending detected ")
