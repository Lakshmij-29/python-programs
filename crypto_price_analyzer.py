
prices = {
    "Bitcoin": 95000,
    "Ethereum": 3200,
    "Solana": 180
}

for coin, price in prices.items():
    print(coin, "- $", price)

highest = max(prices, key=prices.get)
lowest = min(prices, key=prices.get)

print("Highest Priced:", highest)
print("Lowest Priced:", lowest)
