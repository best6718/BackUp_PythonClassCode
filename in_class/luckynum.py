import random

aNum = random.randint(1,100)
guess = input("Please enter a number between 1 and 100: ")
guess = float(guess)
if aNum > guess:
    print("Guess higher!")
elif aNum < guess:
    print("Guess lower!")
else:
    print("You got it! You're lucky!")
