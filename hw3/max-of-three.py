"""
Karena Huang
CS80K Python
2/12/19
max-of-a=three.py
"""
x = 19
y = 15
z = 5

if (x > y) and (x > z):
    print("x is max")
elif (x > y or x < y) and (x < z and z > y):
    print("z is max")
elif (x < y) and (y > z):
    print("y is max")
