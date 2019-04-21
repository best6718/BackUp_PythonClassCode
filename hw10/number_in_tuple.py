"""
Karena Huang
CS80 Python
4/16/19
number_in_tuple.py
"""
theTuple = (9, 5, 100, 72, 10, 999, 875, 43, 81, 1)
number = int(input('Please enter guess a number from the tuple: '))
if number in theTuple:
    print('You got it!')
else:
    print('Nope!')
    
