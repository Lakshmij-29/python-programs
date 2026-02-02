contacts = {}

while True:
    print("1.Add 2.Search 3.View All 4.Exit")
    ch = input()

    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
    elif ch == "2":
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))
    elif ch == "3":
        print(contacts)
    else:
        break
