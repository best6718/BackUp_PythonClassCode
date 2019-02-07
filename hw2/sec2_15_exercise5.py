celsius = input("Please input a temperature in Celsius: ")	
#user asked for temperature
celsius = float(celsius)
#input casted as float in case it was in form of decimals
fahrenheit = celsius*(9/5) + 32
#input was calculated into fahrenheit using fahrenheit formula and assigned to fahrenheit variable
celsius = str(celsius)
#celsius input was casted into string again
fahrenheit = str(fahrenheit)
#fahrenheit that was calculated is casted into string as well
print(celsius + " converted to degrees Fahrenheit is: " + fahrenheit)
#final result is printed out as string
