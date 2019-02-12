"""
Karena Huang
CS80K Python
2/12/19
max-of-any-three.py
"""
x = 3
y = 23
z = 5
if (x == y):
    if (x == z):
        print("They are all equal and greatest")
    elif (x != z) and (x > z):
        print("x and y are equal and greatest")
    elif (z > x):
        print("z is the greatest")
elif (x > y):
    if (x == z):
        print("x and z are equal and greatest")
    elif (x > z):
        print("x is the greatest")
    elif(x < z):
        print("z is the greatest")
elif (x < y):
    if (y == z):
        print("y and z are equal and greatest")
    elif (y > z):
        print("y is the greatest")
    elif(y < z):
        print("z is the greatest")
