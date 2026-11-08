
previous_customers = 1200
retained_customers = 960
new_customers = 250

retention = retained_customers / previous_customers * 100
churn = 100 - retention

print("Previous Customers:", previous_customers)
print("Retained Customers:", retained_customers)
print("New Customers:", new_customers)
print("Retention Rate:", round(retention, 2), "%")
print("Churn Rate:", round(churn, 2), "%")
