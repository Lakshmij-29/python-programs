import random

number = random.randint(1, 10)

print("Guess the number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == number:
    print(" Correct guess!")
else:
    print(" Wrong guess")
    print("Number was:", number)