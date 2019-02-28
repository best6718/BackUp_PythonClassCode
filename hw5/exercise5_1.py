"""
Karena Huang
CS80K Python
2/26/19
exercise5_1.py
"""
total = 0
count = 0
totalAvg = 0
while True:
    aNum = input("Enter a number: ")
    if(aNum == "done"):
        totalAvg = total/count
        #round to 2 places
        totalAvg = round(totalAvg, 2)
        total = str(total)
        count = str(count)
        totalAvg = str(totalAvg)
        print(total + " "+ count + " " + totalAvg)
        break
    try:
        aNum = int(aNum)
    except:
        print("Invalid input")
        continue
    total = total + aNum
    count += 1
    
        
