num = input("Enter number: ")
count = 0

for d in num:
    if int(d) > 5:
        count += 1

print("Digits > 5:", count)
