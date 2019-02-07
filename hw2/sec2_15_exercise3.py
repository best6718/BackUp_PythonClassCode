hours = input("Enter Hours: ")	#user is asked to enter hours
rate = input("Enter Rate: ")		#user is asked to enter rate
hours = float(hours)		#since hours is taken as a string, casting it
					#as float in case it was given as decimal
rate = float(rate)			#same is applied to rate
pay = hours*rate			#hours multiplied with rate to calculate pay
pay = round(pay, 2)		#pay is rounded to 2 decimal places after 
					#calculating it
pay = str(pay)			#pay is casted as a string 
print("Pay: " + pay)		#pay is printed out
