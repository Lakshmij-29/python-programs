amount = float(input("Cart amount: "))
member = input("Premium member? yes/no: ").lower()

discount = 0

if amount > 5000:
    discount += 10
if member == "yes":
    discount += 5

final = amount - (amount * discount / 100)

print("Discount:", discount, "%")
print("Final amount:", final)
