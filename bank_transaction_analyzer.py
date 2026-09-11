transactions = [1200, -450, 3000, -800, -250, 5000]

credits = sum(x for x in transactions if x > 0)
debits = abs(sum(x for x in transactions if x < 0))
balance = credits - debits

print("Total Credits:", credits)
print("Total Debits:", debits)
print("Net Balance:", balance)

if balance < 0:
    print("Account requires attention")
