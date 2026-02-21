num = input("Enter number: ")
power = len(num)
total = 0

for d in num:
    total += int(d) ** power

print("Armstrong" if total == int(num) else "Not Armstrong")
