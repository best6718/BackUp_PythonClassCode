def fibo():
    theList = []
    userInput = input("Please enter a number: ")
    userInput = int(userInput)
    count = 0
    firstNum = 1
    secNum = 1
    if(userInput == 1):
        theList.append(firstNum)
        print(theList)
    elif(userInput == 2):
        theList.append(firstNum)
        theList.append(secNum)
        print(theList)
    else:
        theList.append(firstNum)
        count += 1
        theList.append(secNum)
        count += 1
        while(count < userInput and userInput > 2):
            currentNum = theList[count-1] + theList[count-2]
            theList.append(currentNum)
            count += 1
        print(theList)

fibo()
