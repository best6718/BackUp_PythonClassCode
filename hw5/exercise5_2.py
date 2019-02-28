"""
Karena Huang
CS80K Python
2/26/19
exercise5_2.py
"""
numList = []
while True:
    aNum = input("Enter a number: ")
    if(aNum == "done"):
        theMin = min(numList)
        theMax = max(numList)
        theMin = str(theMin)
        theMax = str(theMax)
        print("This is the min: " + theMin + ". And this is the max of the \
list: " + theMax)
        break
    try:
        aNum = int(aNum)
    except:
        print("Invalid input, try again")
        continue
    numList.append(aNum)
