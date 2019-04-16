"""
Karena Huang
CS80K Python
4/9/19
hw9.py
"""
#Chapter 9, exercise 2
def dayOfMail():
    fileName = input("Enter a file name: ")
    theFile = open(fileName)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    l = len(days)
    days_dictionary = dict()

    for i in days:
        days_dictionary[i] = 0
    
    for lines in theFile:
        if(lines.startswith('From')):
            words = lines.split()
            for word in range(len(words)):
                if (word == 2): 
                    day = words[word]
                    days_dictionary[day] += 1
    print(days_dictionary)
#dayOfMail()

#Chapter 9, exercise 3
def histogram():
    fileName = input("Enter a file name: ")
    theFile = open(fileName)

    email_list = dict()

    for line in theFile:
        if (line.startswith('From')):
            words = line.split()
            for word in range(len(words)):
                if (word == 1):
                    if words[word] not in email_list:
                        email_list[words[word]] = 1
                    else:
                        email_list[words[word]] += 1
    print(email_list)
histogram()
