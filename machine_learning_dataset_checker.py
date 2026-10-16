
dataset = [
    {"age": 22, "salary": 30000},
    {"age": 25, "salary": 45000},
    {"age": None, "salary": 38000},
    {"age": 29, "salary": None}
]

for index, row in enumerate(dataset, start=1):
    missing = [key for key, value in row.items() if value is None]
    if missing:
        print("Row", index, "- Missing:", missing)

print("Total Records:", len(dataset))
print("Complete Records:", sum(all(v is not None for v in row.values()) for row in dataset))
