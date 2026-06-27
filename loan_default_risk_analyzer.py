income = int(input("Monthly income: "))
emi = int(input("Monthly EMI: "))

ratio = emi / income

print("EMI Ratio:", round(ratio, 2))

if ratio > 0.5:
    print("High Default Risk")
else:
    print("Low Default Risk")
