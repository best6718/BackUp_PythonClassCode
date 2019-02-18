#asks user to input year
year = input("Enter the year: ")
#asks user to input name
name = input("Enter your name: ")
#asks user to input age
age = input("Enter your age: ")
#asks user if they already had their birthday
bday = input("Did you already have your bday this year? (Y or N): ")
#casts the input from years into an int
year = int(year)
#casts the input from age into an int
age = int(age)

try:
#if user inputs with the bday variable any of these strings, do this
    if (bday == "N" or bday == "n" or bday == "no" or bday == "No"):
        #create new variable yearBorn calculate year born without factoring in
        #this year, so add 1
        yearBorn = year - (age + 1)
        #cast yearBorn into a string so it's possible to include in print statement
        #later
        yearBorn = str(yearBorn)
        #print out what we need
        print("Hello " + name + ", you were born in the year " + yearBorn + "\n" +
              "Have a great birthday this year!")

    #if user inputs with the bday variable any of these strings, do this
    elif (bday == "Y" or bday == "y" or bday == "yes" or bday == "Yes"):
        #declare new variable yearBorn calculate yearborn factoring in
        #current year
        yearBorn = year - age
        #cast yearBorn as string to include in print statement later
        yearBorn = str(yearBorn)
        #print what we need
        print("Hello " + name + ", you were born in the year " + yearBorn + "\n" +
              "Happy delayed birthday.")
    
#if user inputs anything else into the bday variable, print out wrong answer
except:
    print("Wrong answer")
