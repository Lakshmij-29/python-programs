def save_password():
    site = input("Website: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{site}:{pwd}\n")

def view_passwords():
    with open("passwords.txt") as f:
        print(f.read())

while True:
    print("1.Save 2.View 3.Exit")
    ch = input()

    if ch == "1":
        save_password()
    elif ch == "2":
        view_passwords()
    else:
        break
