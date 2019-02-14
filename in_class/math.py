#be aware we're gonna be listening, using functions from this module
#import math module and random module
import math
import random 

print('Math Module')
#3 returned
print(math.floor(3.45))

#4 returned
print(math.ceil(3.45))

#6 returned
print(math.factorial(3))

#16.0 returned
print(math.pow(2,4))

#8.0 returned
print(math.sqrt(64))

#testing random module
print('Random Module')
#random function in random module, given decimal between 0 and 1
print(random.random())

#including 7!!! 
print(random.randint(5,7)) 

# one trick to round decimal number 
n = random.random()
print(n)

#everytime u call random, ugly number given.. like 0.456786
#if wanna reduce amt of decimal pts in number, take number multiply with 100,
#we get 45.6786, then take the floor of that, we get 45, if we divide by 100
#get 0.45
n = math.floor(n*100)/100
print(n)
