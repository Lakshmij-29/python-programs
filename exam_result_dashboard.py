
marks = [85, 72, 91, 66, 58]

passed = [m for m in marks if m >= 40]

print("Total Students:", len(marks))
print("Passed Students:", len(passed))

topper = max(marks)
print("Highest Marks:", topper)

print("Pass Percentage:",
      (len(passed)/len(marks))*100)
