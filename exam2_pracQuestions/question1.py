def sumAndSequence():
    print("Calculate the n terms of the Arithmetic sequence")
    try:
        a = input("Enter the parameter a: ")
        a = int(a)
        d = input("Enter parameter d: ")
        d = int(d)
        n = input("How many terms do you want to calculate? ")
        n = int(n)
    except:
        print("That was not a number, please try again.")
    
    count = 0
    theSequence = list()
    currentSum = 0
    totalSum = 0
    while(count < n):
        currentSum = 1 + d*(a-1)
        totalSum += currentSum
        theSequence.append(currentSum)
        a += 1
        count += 1
    totalSum = str(totalSum)
    print("This is the entire sequence: ")
    print(theSequence)
    print("The Sum is: " + totalSum)

sumAndSequence()
