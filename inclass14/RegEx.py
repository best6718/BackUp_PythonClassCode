import re

myString = 'Python is awesome \n Python is fun\n'

###Simple search ###
if re.search('Python', myString):
    print('Yes')

###Read ines in a file and only prints the line if fthe pattern is found ###
print('\nSentences containing the pattern Python:')
f = open('readme.txt')

#read one line at a time
for line in f:
    line = line.rstrip()    #removes the end of line character at end of sentence
    if re.search('Python', line):
        print(line)

