"""
Karena Huang
CS80K Python
3-21-19
exam2_karenahuang.py
"""
print("Calculate the n terms of the Geometric sequence")
try:
    a = int(input("Enter the parameter a: "))
    r = int(input("Enter parameter r: "))
    n = int(input("How many terms do you want to calculate? "))
except:
    print("That was not a number, please try again.")
    
theSequence = list()
currentProduct = 0
totalSum = 0
i = 1
for j in range(n):
    currentProduct = a * r**(i-1)
    i += 1
    totalSum += currentProduct
    theSequence.append(currentProduct)
totalSum = str(totalSum)
print(theSequence, end=" ")
print("The Sum is: " + totalSum)
