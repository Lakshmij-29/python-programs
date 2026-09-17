returns = {
    "Laptop": 12,
    "Phone": 25,
    "Tablet": 8,
    "Headphones": 31
}

for product, count in returns.items():
    status = "High Returns" if count > 20 else "Normal Returns"
    print(product, "-", count, "-", status)

highest = max(returns, key=returns.get)
print("Most Returned:", highest)
