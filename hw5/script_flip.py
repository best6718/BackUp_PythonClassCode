"""
Karena Huang
CS80K Python
2/26/19
script_flip.py
"""
import random
heads = 0
tails = 0
flips = 0
flipNumber = input("How many coin flips do you want? ")
flipNumber = int(flipNumber)
while(flips != flipNumber):
    headsOrTails = random.randint(0, 1)
    if(headsOrTails == 1):
        heads += 1
    else:
        tails += 1
    flips += 1
heads = str(heads)
tails = str(tails)
print("The number of heads you had was: " + heads + ". And the number \
of tails you had was: " + tails)
