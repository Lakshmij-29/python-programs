
files = [
    "report.pdf", "data.csv", "report.pdf",
    "image.png", "notes.txt", "data.csv"
]

seen = set()
duplicates = set()

for filename in files:
    if filename in seen:
        duplicates.add(filename)
    seen.add(filename)

print("Total Files:", len(files))
print("Unique Files:", len(seen))
print("Duplicate Names:", sorted(duplicates))
