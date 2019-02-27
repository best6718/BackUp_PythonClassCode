'''
Review and practice
Special characters in python:  "  '  \  
By the way, this is a multi-line comment  
'''

# Escape character \
# Different ways to output: I've said:  “Python is friendly”
print("I've said: \"Python\"")
print('I\'ve said: "Python"')  


# multi-line strings 
print()
my_string = """Hello, 
I will be arriving late for dinner"""
print(my_string)

print()
my_string = "Hello, \nI will be arriving late for dinner"
print(my_string)


# This is not a multi-line string
#this backslash here is just to make the code neater and cleaner! 
print()
my_string = "Hello, \
I will be arriving late for dinner"
print(my_string)

# same as 
print('Same as')
print("Hello, \
I will be arriving late for dinner")
