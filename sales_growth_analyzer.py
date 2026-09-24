previous_sales = 420000
current_sales = 485000

growth = ((current_sales - previous_sales) / previous_sales) * 100

print("Previous Sales:", previous_sales)
print("Current Sales:", current_sales)
print("Growth Rate:", round(growth, 2), "%")

if growth > 10:
    print("Strong Sales Growth")
else:
    print("Moderate Sales Growth")
