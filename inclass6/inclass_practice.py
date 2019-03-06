word = input("Please enter a word: ")
fileName = input("Please enter a file name: ")
count = 0
x = open(fileName, 'r')
for line in fileName:
    for eachWord in line:
        if(eachWord == word):
            count++
            print(line)
print(count)
