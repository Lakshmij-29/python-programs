
target = 500000

sales = {
    "January": 420000,
    "February": 530000,
    "March": 480000,
    "April": 610000
}

for month, amount in sales.items():
    status = "Achieved" if amount >= target else "Missed"
    print(month, "-", amount, "-", status)

print("Best Month:", max(sales, key=sales.get))
