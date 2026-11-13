
transactions = [
    ("TX101", 2500),
    ("TX102", 4500),
    ("TX103", 2500),
    ("TX104", 8000),
    ("TX101", 2500)
]

seen = set()

for transaction in transactions:
    if transaction in seen:
        print("Duplicate Detected:", transaction)
    else:
        seen.add(transaction)

print("Total Transactions:", len(transactions))
print("Unique Transactions:", len(seen))
