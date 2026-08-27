stocks = {
    "TCS": 3850,
    "INFY": 1920,
    "HDFC": 1780,
    "RELIANCE": 2950
}

average = sum(stocks.values()) / len(stocks)
highest = max(stocks, key=stocks.get)

print("Average Price:", round(average, 2))
print("Highest Stock:", highest)

for name, price in stocks.items():
    print(name, ":", price)
