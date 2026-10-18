
portfolio = {
    "Stock_A": [100, 120, 10],
    "Stock_B": [200, 185, 5],
    "Stock_C": [150, 165, 8]
}

total_profit = 0

for stock, data in portfolio.items():
    bought, current, quantity = data
    profit = (current - bought) * quantity
    total_profit += profit
    print(stock, "Profit/Loss:", profit)

print("Portfolio Profit/Loss:", total_profit)
