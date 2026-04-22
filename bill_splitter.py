bill = float(input("Enter total bill: "))
people = int(input("Enter number of people: "))
tip = float(input("Enter tip %: "))

final = bill + (bill * tip / 100)
share = final / people

print("Total with tip:", final)
print("Each person pays:", round(share, 2))
