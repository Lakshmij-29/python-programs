sales = float(input("Monthly sales: "))

if sales >= 100000:
    commission = sales * 0.10
elif sales >= 50000:
    commission = sales * 0.05
else:
    commission = sales * 0.02

print("Commission:", commission)
print("Calculation Complete")
