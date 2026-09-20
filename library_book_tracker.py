books = {
    "Python Basics": True,
    "Data Science": False,
    "Machine Learning": True,
    "SQL Guide": False
}

for book, available in books.items():
    status = "Available" if available else "Borrowed"
    print(book, "-", status)

available_books = sum(books.values())
print("Available Books:", available_books)
