"""
Karena Huang
CS80K Python
3/12/19
Easter_Egg.py
"""
def EasterEgg():
    userInput = input("Please enter a file name: ")
    number = 0
    if(userInput == "na na boo boo"):
        userInput = userInput.upper()
        print(userInput + " - You have been punk'd!")
        return
    try:
        theFile = open(userInput)
    except:
        print("File cannot be opened: ", userInput)
        return
    for eachLine in theFile:
        if(eachLine.endswith('\n')):
            number += 1
    number = str(number)
    print("The file was " + number + " lines long.")
EasterEgg()
