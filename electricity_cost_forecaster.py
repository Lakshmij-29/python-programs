monthly_usage = [420, 450, 470, 510, 490]

average = sum(monthly_usage) / len(monthly_usage)
forecast = average * 7.5

print("Average Monthly Usage:", round(average, 2), "kWh")
print("Estimated Monthly Cost:", round(forecast, 2))
print("Highest Usage:", max(monthly_usage), "kWh")

if forecast > 4000:
    print("High Energy Cost Expected")
