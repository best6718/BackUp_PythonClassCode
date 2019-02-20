# while loop 
# allow a limited amount of guesses 
# don't allow non numbers guesses 

import random

howManyTimes = 0
print('Hello')

# We assume that the you are not lucky until you prove it
lucky = 0

print('What is your name?')
yourName = input()

number = random.randint(1, 100)

print('Hi ' + yourName + ' how lucky are you? (Lucky or Not)')
howLucky = input()

print( yourName + ' can you pick a number between 1 and 100')
print('Take a guess.')

while howManyTimes < 5:

    your_number = input()

    try:
        your_number = int(your_number)
    
    except:
        print("You didn't enter a number!\nTry again.")
        continue
    
    howManyTimes += 1
    triesLeft = 5 - howManyTimes
    triesLeft = str(triesLeft)
    
    if your_number < number:
        print('Guess higher') 
        print('You have: ' + triesLeft + ' tries left')
    if your_number > number:
        print('Guess lower')
        print('You have: ' + triesLeft + ' tries left')
    if your_number == number:
        print('YOU ARE LUCKY :-) ' + yourName)
        howManyTimes = str(howManyTimes)
        print('It took you '+ howManyTimes + ' times to guess the number!')
        lucky = 1
        break

if lucky == 0:
    number = str(number)
    print('YOU WERE NOT LUCKY THIS TIME :-(  The rignt number is ' + number)
