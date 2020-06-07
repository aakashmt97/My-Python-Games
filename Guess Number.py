import random

guessTaken = 0

name = input("What is your Name: ")

print("Well, " + name + " I'm thinking of a number between 1 to 20")

number = random.randint(1, 20)

for guessTaken in range(6):

    guess = int(input("Guess the number: "))

    if guess < number:
        print("Your guess is too low")

    if guess > number:
        print("Your guess is too high")

    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken + 1)
    print("Good Job " + name + "!! You guessed the number in " + guessTaken +
          " guesses!")

if guess != number:
    number = str(number)
    print("Sorry " + name + ", the number I was guessing is " + number + ".") 
