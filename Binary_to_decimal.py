binary = input("Enter binary number: ")
decimal = 0

for d in binary:
    decimal = decimal * 2 + int(d)

print("Decimal value:", decimal)
