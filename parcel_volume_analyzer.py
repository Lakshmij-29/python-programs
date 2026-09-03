parcels = [45, 62, 51, 78, 69, 55]

total = sum(parcels)
average = total / len(parcels)
peak = max(parcels)

print("Total Parcels:", total)
print("Average Daily Parcels:", round(average, 2))
print("Peak Volume:", peak)

if peak > 70:
    print("High parcel volume detected")
