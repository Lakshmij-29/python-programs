import csv

file = open("data.csv", "r")
reader = csv.DictReader(file)

data = []

for row in reader:
    data.append(row)

print("Converted Data:")
for item in data:
    print(item)

file.close()
