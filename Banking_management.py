balance = 1000

while True:
    print("1.Deposit 2.Withdraw 3.Check 4.Exit")
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