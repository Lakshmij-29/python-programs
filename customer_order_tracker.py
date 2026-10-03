
orders = {
    "ORD101": "Delivered",
    "ORD102": "Processing",
    "ORD103": "Cancelled",
    "ORD104": "Delivered"
}

delivered = list(orders.values()).count("Delivered")
pending = list(orders.values()).count("Processing")

print("Total Orders:", len(orders))
print("Delivered:", delivered)
print("Processing:", pending)
