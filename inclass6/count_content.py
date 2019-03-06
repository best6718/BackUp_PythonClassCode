myfile =  open('readme.txt')
 
count = 0
content = myfile.read()
for c in content:    # read the file one line at a time
    print(c)
    count +=  1
print(count)

myfile.close() 
