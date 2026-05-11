students = ["Aman", "Riya", "John", "Neha"]
present = ["Aman", "John"]

for student in students:
    if student in present:
        print(student, ": Present ")
    else:
        print(student, ": Absent ")

attendance = (len(present) / len(students)) * 100
print("Attendance Percentage:", attendance)
