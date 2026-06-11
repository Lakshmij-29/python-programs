used = float(input("Used storage (GB): "))
total = float(input("Total storage (GB): "))

usage = (used / total) * 100

print("Storage Usage:", round(usage, 2), "%")

if usage > 80:
    print("Storage nearing capacity")
else:
    print("Storage level normal")
