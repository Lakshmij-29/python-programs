amount = float(input("Enter bill amount: "))

if amount > 5000:
    discount = 0.2
elif amount > 2000:
    discount = 0.1
else:
    discount = 0

final = amount - (amount * discount)
print("Final Amount:", final)