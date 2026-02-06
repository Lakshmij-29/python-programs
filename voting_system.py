votes = {"A":0, "B":0, "C":0}

while True:
    choice = input("Vote A/B/C or exit: ").upper()
    if choice == "EXIT":
        break
    if choice in votes:
        votes[choice] += 1

print("Final Votes:", votes)