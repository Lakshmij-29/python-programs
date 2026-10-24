
values = [22, 25, 27, 24, 26, 23, 150, 28, 21]

average = sum(values) / len(values)
outliers = [value for value in values if abs(value - average) > 30]

print("Dataset Average:", round(average, 2))
print("Potential Outliers:", outliers)
print("Total Records:", len(values))
print("Outlier Count:", len(outliers))
