subscriptions = {
    "Basic": 120,
    "Standard": 85,
    "Premium": 45
}

prices = {
    "Basic": 299,
    "Standard": 599,
    "Premium": 999
}

revenue = sum(subscriptions[p] * prices[p] for p in subscriptions)

print("Monthly Revenue:", revenue)
print("Total Subscribers:", sum(subscriptions.values()))

for plan, count in subscriptions.items():
    print(plan, "-", count)
