
students = {
    "Aman": [78, 85, 91],
    "Riya": [92, 88, 95],
    "Kiran": [45, 56, 62],
    "Neha": [35, 42, 38]
}

for name, marks in students.items():
    average = sum(marks) / len(marks)
    result = "Pass" if min(marks) >= 40 else "Fail"
    print(name, round(average, 2), result)

topper = max(students, key=lambda n: sum(students[n]))
print("Top Performer:", topper)
