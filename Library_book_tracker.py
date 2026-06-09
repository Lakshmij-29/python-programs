books = {
    "Python_Basics": True,
    "Data_Science": False,
    "Machine_Learning": True
}

for title, available in books.items():
    status = "Available" if available else "Issued"
    print(title, "-", status)

print("Library inventory checked")
