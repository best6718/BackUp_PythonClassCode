"""
Karena Huang
CS80K Python
4/16/19
problem10_1.py
"""
import operator
fileName = input("Enter a file name: ")
theFile = open(fileName)

email_dict = dict()

for line in theFile:
    if (line.startswith('From')):
        words = line.split()
        for word in range(len(words)):
            if (word == 1):
                if words[word] not in email_dict:
                    email_dict[words[word]] = 1
                else:
                    email_dict[words[word]] += 1
emailList = list(email_dict.items())
print("This is the list of tuples from the dictionary: ")
print(emailList)
print(" ")

emailList.sort(key = operator.itemgetter(1))
lastElement = emailList[-1]
print("This is the list sorted: ")
print(emailList)
print(" ")
print("This is the person with the most commits: ")
print(lastElement)

emailList.reverse()
print("This is the list reversed: ")
print(emailList)
print("This is the person with the most commits: ")
firstElement = emailList[0]
print(firstElement)

