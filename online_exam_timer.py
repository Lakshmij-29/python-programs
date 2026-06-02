import time

seconds = 5

while seconds > 0:
    print("Time Left:", seconds)
    time.sleep(1)
    seconds -= 1

print("Exam submitted automatically")
