courses = {"CS101": 0, "DS102": 0, "AI103": 0}
limit = 2

while True:
    print("Courses:", courses)
    ch = input("Register course code or exit: ")

    if ch == "exit":
        break
    if ch in courses and courses[ch] < limit:
        courses[ch] += 1
        print("Registered")
    else:
        print("Course full or invalid")