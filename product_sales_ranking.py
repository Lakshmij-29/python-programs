sales = {
    "Laptop": 15,
    "Phone": 30,
    "Tablet": 10
}

sorted_sales = sorted(sales.items(),
                      key=lambda x: x[1],
                      reverse=True)

for product, count in sorted_sales:
    print(product, "-", count, "units sold")
