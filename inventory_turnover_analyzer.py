sold = 450
average_inventory = 120

turnover = sold / average_inventory

print("Inventory Turnover Ratio:",
      round(turnover, 2))

if turnover > 3:
    print("Inventory Moving Fast")
else:
    print("Slow Inventory Movement")
