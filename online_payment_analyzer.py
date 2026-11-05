
payments = {
    "UPI": 45000,
    "Card": 32000,
    "Net Banking": 18000,
    "Wallet": 12000
}

total = sum(payments.values())

for method, amount in payments.items():
    share = amount / total * 100
    print(method, "-", round(share, 2), "%")

print("Total Payments:", total)
print("Most Used Method:", max(payments, key=payments.get))
