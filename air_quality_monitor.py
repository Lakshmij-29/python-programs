aqi_values = [82, 95, 110, 76, 125]

average = sum(aqi_values) / len(aqi_values)
unhealthy = [aqi for aqi in aqi_values if aqi > 100]

print("Average AQI:", round(average, 2))
print("Unhealthy Readings:", len(unhealthy))

if average > 100:
    print("Air quality needs attention")
