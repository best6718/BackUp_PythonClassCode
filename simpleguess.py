mynum = 30
num = input("Guess a number between 1 and 100: ")

try:
    num = int(num)
    
    if num == mynum:
        print("You are lucky!")

    else:
        if num < mynum:
            print("Too low!")
        else:
            print("Too high!")
except:
    print("Please enter an integer")
print("does this run")
