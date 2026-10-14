
cash_balance = float(input("Available Cash: "))
monthly_expenses = float(input("Monthly Expenses: "))
monthly_revenue = float(input("Monthly Revenue: "))

burn_rate = monthly_expenses - monthly_revenue

if burn_rate > 0:
    runway = cash_balance / burn_rate
    print("Estimated Runway:", round(runway, 2), "months")
elif burn_rate < 0:
    print("Startup is generating a monthly surplus")
else:
    print("Revenue covers monthly expenses")
