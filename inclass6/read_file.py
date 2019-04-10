# Open a file 
myfile =  open('readme.txt')

print('Here is the file handle: ' + str(myfile) + ' of type ' + str(type(myfile)))      # myfile is a reference to the file
                                                                                        # file handle     
# Read the entire content of the file 
content = myfile.read()     #content is now a string  
print('Content is of type: ' + str(type(content)))

# len gives the number of charactes in a file 
print('The length of the file is ' + str(len(content)))

# print the entire file 
print('\nAnd here is the content of the file: \n\n' + content + 'characters')

myfile.close()  # what is we don't close the file? 
