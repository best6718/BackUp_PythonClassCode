thefile = open('readme.txt')
content = thefile.read()
content = content.split()
thedict = dict()
for words in content:
    if words not in thedict:
        thedict[words] = 1
        
