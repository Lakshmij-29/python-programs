sales = [12000, 15000, 17000, 20000]

growth = 0.10
last_month = sales[-1]

forecast = last_month + (last_month * growth)

print("Previous Sales:", sales)
print("Forecasted Sales:", forecast)

if forecast > 22000:
    print("High growth expected")
else:
    print("Moderate growth expected")
