routes = {
    "Route_A": 12,
    "Route_B": 8,
    "Route_C": 15
}

fastest = min(routes, key=routes.get)

print("Best Route:", fastest)
print("Travel Time:", routes[fastest], "minutes")
print("Route Analysis Complete")
