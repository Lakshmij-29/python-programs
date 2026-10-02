
storage = {
    "Images": 24.5,
    "Videos": 68.2,
    "Documents": 12.8,
    "Backups": 35.4
}

total = sum(storage.values())
largest = max(storage, key=storage.get)

print("Total Storage:", round(total, 2), "GB")
print("Largest Category:", largest)

for category, size in storage.items():
    print(category, "-", size, "GB")
