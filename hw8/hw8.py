"""
Karena Huang
CS80K Python
3-19-19
hw8.py
"""
#Chapter 7, exercise 2
def avgSpam():
    fname = input("Enter the file name: ")
    theFile = open(fname)
    currentSpamValue = 0
    count = 0
    avgSpamValue = 0
    for eachLine in theFile:
        if eachLine.startswith('X-DSPAM-Confidence:'):
            delimiter = ' '
            spamArray = eachLine.split(delimiter)
            spamValue = spamArray[1]
            spamValue = float(spamValue)
            currentSpamValue = currentSpamValue + spamValue
            count += 1
    avgSpamValue = currentSpamValue/count       
    avgSpamValue = str(avgSpamValue)
    print("Average spam confidence: " + avgSpamValue)

avgSpam()

#Chapter 8, Exercise 4
def romeo():
    theList = list()
    theFile = open('romeo.txt')
    for eachLine in theFile:
        romeoArray = eachLine.split()
        for theElement in romeoArray:
            if (theElement in romeoArray not in theList):
                theList.append(theElement)
            else:
                continue
    theList.sort()
    print(theList)

romeo()

#Chapter 8, Exercise 5
def fromcount():
    fileName = input("Enter a file name: ")
    count = 0
    lineArray = list()
    theFile = open(fileName)
    for eachLine in theFile:
        if eachLine.startswith('From '):
            mailArray = eachLine.split()
            emailAddress = mailArray[1]
            lineArray.append(emailAddress)
            count += 1
    for eachElement in lineArray:
        print(eachElement)
    count = str(count)
    print("There were " + count + " lines in the file with From as the first word")

fromcount()  

#Chapter 8, Exercise 6
def listOfNum():
    numList = list()
    while True:
        aNum = input("Enter a number: ")
        numList.append(aNum)
        if(aNum == "done"):
            numList.remove("done")
            break
        try:
            aNum = int(aNum)
        except:
            print("Invalid input, try again")
            continue
    theMin = min(numList)
    theMax = max(numList)
    theMin = str(theMin)
    theMax = str(theMax)
    print("Maximum: " + theMax)
    print("Minimum: " + theMin)

listOfNum()








