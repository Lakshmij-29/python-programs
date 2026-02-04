def register():
    u = input("Username: ")
    p = input("Password: ")
    with open("users.txt", "a") as f:
        f.write(f"{u},{p}\n")

def login():
    u = input("Username: ")
    p = input("Password: ")
    with open("users.txt") as f:
        for line in f:
            user, pwd = line.strip().split(",")
            if u == user and p == pwd:
                print("Login success")
                return
    print("Login failed")

while True:
    print("1.Register 2.Login 3.Exit")
    ch = input()

    if ch == "1":
        register()
    elif ch == "2":
        login()
    else:
        break