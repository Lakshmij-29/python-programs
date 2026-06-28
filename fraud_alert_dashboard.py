transactions = [2500, 80000, 1200, 95000, 500]

alerts = 0

for amount in transactions:
    if amount > 50000:
        alerts += 1
        print("Alert:", amount)

print("Total Alerts:", alerts)
print("System Scan Complete")
