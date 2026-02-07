seats = {i: "Available" for i in range(1, 11)}

def show_seats():
    for seat, status in seats.items():
        print(f"Seat {seat}: {status}")

def book_seat():
    seat = int(input("Choose seat number: "))
    if seats.get(seat) == "Available":
        seats[seat] = "Booked"
        print("Seat booked successfully")
    else:
        print("Seat not available")

while True:
    print("1.Show Seats 2.Book Seat 3.Exit")
    ch = input()

    if ch == "1":
        show_seats()
    elif ch == "2":
        book_seat()
    else:
        break