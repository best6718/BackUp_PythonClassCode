# allow a limited amount of guesses 
# while loop 

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
    your_number = int(your_number)

    howManyTimes += 1

    if your_number < number:
        print('Guess higher') 

    if your_number > number:
        print('Guess lower')

    if your_number == number:
        print('YOU ARE LUCKY :-) ' + yourName)
        howManyTimes = str(howManyTimes)
        print('It took you '+ howManyTimes + ' times to guess the number!')
        lucky = 1
        break

if lucky == 0:
    number = str(number)
    print('YOU WERE NOT LUCKY THIS TIME :-(  The right number is ' + number)
