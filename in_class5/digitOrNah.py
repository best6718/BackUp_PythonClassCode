number = input("Please enter a number: ")
digitOrNot = number.isdigit()
if (digitOrNot == True):
    print("You entered the number: " + number)
else:
    while(digitOrNot != True):
        tryAgain = input("Please enter a number again: ")
        digitOrNot = tryAgain.isdigit()
    print("You entered the number: " + tryAgain)


"""
while True:
    num = input('Please enter a number: ')
    if num.isdigit():
        print('You entered the number ' + num)
        break
"""

