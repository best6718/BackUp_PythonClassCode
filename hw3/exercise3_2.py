"""
Karena Huang
CS80K Python
2/12/19
exercise3_2.py
"""
hours = input("Enter Hours: ")	#user is asked to enter hours
rate = input("Enter Rate: ")		#user is asked to enter rate
try:
    hours = float(hours)		#since hours is taken as a string, casting it
                                    #as float in case it was given as decimal
except:
    print("Error, please enter numeric input")
try:
    rate = float(rate)			#same is applied to rate
except:
    print("Error, please enter numeric input")
if (hours > 40):        #if hours are greater than 40
    overForty = hours - 40      #save amount greater than 40 into variable
    overTime = (rate*1.5)*overForty #use that variable, multiply with 1.5 times hourly rate 
    underFortyOne = 40*rate     #what's left will be 40 hours, multiplied with hourly rate
    pay = overTime + underFortyOne #add together the two calculations to get total pay
else:
    pay = rate*hours
pay = round(pay, 2)		#pay is rounded to 2 decimal places after 
					#calculating it
pay = str(pay)			#pay is casted as a string 
print("Pay: " + pay)		#pay is printed out
