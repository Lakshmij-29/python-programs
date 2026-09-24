records = [
    {"name": "Aman", "age": 21},
    {"name": "Riya", "age": None},
    {"name": "John", "age": 24},
    {"name": "", "age": 22}
]

missing = 0

for record in records:
    if not record["name"] or record["age"] is None:
        missing += 1
        print("Incomplete Record:", record)

print("Total Records:", len(records))
print("Incomplete Records:", missing)
