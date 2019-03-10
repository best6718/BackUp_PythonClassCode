word = input("Please enter a word: ")
fileName = input("Please enter a file name: ")
count = 0

#she had
#fileName = open(file) which i guess is the same as what we have

x = open(fileName, 'r')

for line in fileName:
    #she had second line of for loop
    #if word in line:
        #print(line) 
    for eachWord in line:
        if(eachWord == word):
            count += 1
            print(line)
            
print(count)
