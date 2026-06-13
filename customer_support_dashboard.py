tickets = {
    "Open": 15,
    "In_Progress": 8,
    "Resolved": 42
}

total = sum(tickets.values())

for status, count in tickets.items():
    percent = (count / total) * 100
    print(status, ":", round(percent, 1), "%")

print("Total Tickets:", total)
