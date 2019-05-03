"""
Karena Huang
CS80K Python
4/25/19
Exam3.py
"""
#Find time for Karena to video game in a day with a busy college schedule
def calcTime(firstTime, secTime):
    timeDiff = secTime - firstTime
    return timeDiff

#using one dictionary here
days = {"Monday": []}

#calling while loop to make sure that there is something in
#mondays values
while(days["Monday"] == []):
    #user input, for loop, list, casting, try except block
    try:
        #string concatenation to save space
        days["Monday"] = [int(x) for x in input("Please enter your " +
                                                "schedule for Monday: ").split()]
        if (not KeyboardInterrupt):
            break
        #conditional statement
        if(days["Monday"] == []):
            raise Exception
    except:
        print("You didn't enter any times, please try again!")
        continue
    
    
#Boolean expression, will be checked at end of code
foundTime = False
#will need count in conditions in for loop below
count = 0
#to compare time differences
previousTime = 0
#to be displayed at end if there's free time
timesFree = []

#saved as a variable for convenience
valuesInMon = days["Monday"]

#need to check time differences for free time
for currentTime in valuesInMon:
    if(calcTime(previousTime, currentTime) > 60 and previousTime > 0):
        foundTime = True
        if(count == 1 or count >= 1):
            timesFree.append(currentTime)
            count += 1
        else:
            timesFree.append(previousTime)
            timesFree.append(currentTime)
            count += 1   
    previousTime = currentTime

#if there is free time, determined by freeTime boolean, do this
if(foundTime):
    print("There will be time today to play video games.")
    print("These are the times that you will have free time to play video games: ")
    print(timesFree)
#otherwise print this
else:
    print("You don't have time for video games today sorry!")

###Test cases:
# Number 1: If you enter the below input upon request for user input, results
# will be positive: 1000 1050 1200 1300 1430 1545

# Number 2: If you enter nothing and just hit return upon request for user input.
# program will keep asking for input
        
