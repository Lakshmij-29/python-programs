purchases = {
    "Aman": [450, 800, 1200],
    "Riya": [900, 1500, 700],
    "John": [300, 450, 600]
}

for customer, amounts in purchases.items():
    total = sum(amounts)
    print(customer, "Total:", total)

top_customer = max(purchases, key=lambda x: sum(purchases[x]))
print("Top Customer:", top_customer)
