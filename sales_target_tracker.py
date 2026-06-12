target = 100000
achieved = float(input("Sales achieved: "))

progress = (achieved / target) * 100

print("Target Completion:", round(progress, 2), "%")

if progress >= 100:
    print("Target achieved")
else:
    print("Target pending")
