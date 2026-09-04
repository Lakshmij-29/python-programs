students = {
    "Aman": [85, 78, 92],
    "Riya": [91, 88, 95],
    "Kiran": [72, 80, 76]
}

for name, marks in students.items():
    average = sum(marks) / len(marks)
    status = "Excellent" if average >= 90 else "Good" if average >= 75 else "Needs Improvement"
    print(name, "-", round(average, 2), "-", status)
