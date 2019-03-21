"""
Karena Huang
CS80K Python
3/13/19
shout.py
"""
#Exercise 7.1
def shout():
    fileName = input("Give us a file name: ")
    theFile = open(fileName)
    for line in theFile:
        line = line.rstrip()
        line = line.upper()
        print(line)

    theFile.close()
shout()

