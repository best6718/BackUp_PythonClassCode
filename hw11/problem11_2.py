"""
Karena Huang
CS80K Python
4/21/19
problem11_2.py
"""
import re

fileName = input("Enter file: ")
theFile = open(fileName)
theSum = 0
theCount = 0
for lines in theFile:
    if lines.startswith("New Revision: "):
        theNumList = re.findall('\d{5}', lines)
        theCount += 1
        #inside list of finding all
        for theNum in theNumList:
            theNum = int(theNum)
            theSum += theNum

theAvg = theSum/theCount
theAvg = str(theAvg)
print(theAvg)
    
