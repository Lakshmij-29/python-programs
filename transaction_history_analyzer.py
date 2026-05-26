transactions = [2500, -500, 4000, -1200, 3200]

credit = sum(t for t in transactions if t > 0)
debit = sum(t for t in transactions if t < 0)

print("Total Credit:", credit)
print("Total Debit:", abs(debit))

balance = credit + debit
print("Net Balance:", balance)
