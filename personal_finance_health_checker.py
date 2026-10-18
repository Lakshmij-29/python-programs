

income = float(input("Monthly Income: "))
expenses = float(input("Monthly Expenses: "))
savings = income - expenses

if income <= 0 or expenses < 0:
    print("Enter valid financial values")
else:
    rate = savings / income * 100
    print("Monthly Savings:", round(savings, 2))
    print("Savings Rate:", round(rate, 2), "%")
    print("Financial Status:", "Healthy" if rate >= 20 else "Needs Improvement")
