
daily_demand = [420, 440, 460, 450, 480, 500]

average = sum(daily_demand) / len(daily_demand)
recent_change = daily_demand[-1] - daily_demand[-2]
forecast = daily_demand[-1] + recent_change

print("Average Demand:", round(average, 2), "MW")
print("Latest Demand:", daily_demand[-1], "MW")
print("Estimated Next Demand:", forecast, "MW")

if forecast > 500:
    print("High Demand Alert")
