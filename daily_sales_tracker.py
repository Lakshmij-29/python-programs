sales = []

for i in range(5):
    amount = float(input("Enter sale amount: "))
    sales.append(amount)

print("Total Sales:", sum(sales))
print("Highest Sale:", max(sales))
print("Average Sale:", sum(sales)/len(sales))
