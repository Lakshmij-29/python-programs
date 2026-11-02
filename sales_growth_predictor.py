
monthly_sales = [45000, 48000, 51000, 54000, 57000]

growth = monthly_sales[-1] - monthly_sales[-2]
forecast = monthly_sales[-1] + growth

average = sum(monthly_sales) / len(monthly_sales)

print("Average Sales:", round(average, 2))
print("Latest Sales:", monthly_sales[-1])
print("Monthly Increase:", growth)
print("Next Month Estimate:", forecast)
