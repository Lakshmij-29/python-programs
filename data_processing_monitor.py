
records = [1200, 1450, 980, 1760, 1320]

total = sum(records)
average = total / len(records)
peak = max(records)

print("Records Processed:", total)
print("Average Batch:", round(average, 2))
print("Largest Batch:", peak)

if peak > 1500:
    print("Large processing batch detected")
