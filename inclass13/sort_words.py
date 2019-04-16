theFile = open('readme.txt')
readFile = theFile.read()
lineSplit = readFile.split()

tuplelist = []

for x in lineSplit:
    newtuple = (len(x), x)
    if newtuple not in tuplelist:
        tuplelist.append(newtuple)

print(tuplelist)
#myList.sort(reverse = True) with list solution

mydict = {}

for x in tuplelist:
    mydict[x[1]] = x[0]

print(mydict)

#################

#theDict = dict()

#readFile = readFile.strip()
#print(readFile)
#readFile = readFile.replace('\n', ' ')

#print(type(lineSplit)
#lineSplit = dict(lineSplit)
#print(lineSplit)


#for elements in lineSplit:
    #if (elements not in thedict):
        #thedict[elements] += 1
