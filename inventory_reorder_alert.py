stock = int(input("Current stock: "))
daily_sales = int(input("Avg daily sales: "))

days_left = stock / daily_sales

print("Stock lasts:", round(days_left, 1), "days")

if days_left < 7:
    print("Reorder now ")
else:
    print("Stock sufficient ")
