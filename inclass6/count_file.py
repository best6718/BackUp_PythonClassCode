myfile =  open('readme.txt')

# Count lines in the file 
count = 0
for line in myfile:    # read the file one line at a time
    print(line)
    count +=  1
    
print("line count", count)

myfile.close() 
