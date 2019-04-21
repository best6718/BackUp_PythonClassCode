"""
Karena Huang
CS80K Python
4/25/19
Exam3.py
"""
#Find time for Karena to video game in a day with a busy college schedule
def calcTime(firstTime, secTime):
    timeDiff = secTime - firstTime
    print(timeDiff)

#using one dictionary here
days = {}

#asking for user input here, also running a for loop here,
#also putting a list in the dictionary
#casting user input into ints
try:
    #string concatenation to save space
    days["Monday"] = [int(x) for x in input("Please enter your " +
                                            "schedule for Monday: ").split()]

except:
    
