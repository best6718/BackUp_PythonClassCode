"""
Karena Huang
CS80K Python
3/5/19
hw6.py
"""

#Exercise6_1
def printBackwards():
    fruit = 'banana'
    index = len(fruit) - 1
    while(index > -1):
        character = fruit[index]
        print(character)
        index -= 1

printBackwards()

#Exercise6_2
#fruit[:] means the entire range of fruit. So the entire value of fruit
#would be printed out

#Exercise6_3
def count():
    word = 'banana'
    theCount = 0
    for letter in word:
        if(letter == 'a'):
            theCount = theCount + 1
    print(theCount)

count()

#Exercise6_5
def theFloatPtNum():
    theString = 'X-DSPAM-Confidence:0.8475'
    atpos = theString.find(':')
    theFloat = theString[atpos+1:]
    print(theFloat)
    theFloat = float(theFloat)

theFloatPtNum()
    
    


