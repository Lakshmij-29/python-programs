
names = [" Aman ", "Riya", "", "Kiran", " Aman ", None]

cleaned = [name.strip() for name in names if name and name.strip()]
unique_names = list(dict.fromkeys(cleaned))

print("Original Records:", len(names))
print("Cleaned Records:", len(cleaned))
print("Unique Names:", len(unique_names))
print("Final Dataset:")

for name in unique_names:
    print(name)
