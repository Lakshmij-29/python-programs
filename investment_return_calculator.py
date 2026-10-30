initial = float(input("Initial Investment: "))
final = float(input("Current Value: "))

profit = final - initial
percentage = profit / initial * 100 if initial > 0 else 0

print("Initial Investment:", initial)
print("Current Value:", final)
print("Profit/Loss:", round(profit, 2))
print("Return:", round(percentage, 2), "%")
