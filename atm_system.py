balance = 5000
pin = "1234"

entered = input("Enter PIN: ")

if entered == pin:
    while True:
        print("1.Deposit 2.Withdraw 3.Balance 4.Exit")
        ch = input()

        if ch == "1":
            balance += int(input("Amount: "))
        elif ch == "2":
            amt = int(input("Amount: "))
            if amt <= balance:
                balance -= amt
        elif ch == "3":
            print("Balance:", balance)
        else:
            break
else:
    print("Wrong PIN")