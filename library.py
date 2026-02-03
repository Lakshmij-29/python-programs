books = []

while True:
    print("1.Add Book 2.Issue Book 3.View 4.Exit")
    ch = input()

    if ch == "1":
        books.append(input("Book name: "))
    elif ch == "2":
        book = input("Book to issue: ")
        if book in books:
            books.remove(book)
            print("Issued")
        else:
            print("Not available")
    elif ch == "3":
        print(books)
    else:
        break