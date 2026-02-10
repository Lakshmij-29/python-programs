import os

while True:
    print("1.List Files 2.Create File 3.Delete File 4.Exit")
    ch = input()

    if ch == "1":
        print(os.listdir())
    elif ch == "2":
        name = input("File name: ")
        open(name, "w").close()
        print("File created")
    elif ch == "3":
        name = input("File name: ")
        if os.path.exists(name):
            os.remove(name)
            print("Deleted")
    else:
        break