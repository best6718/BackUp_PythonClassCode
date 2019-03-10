''' short.txt 
This is a short file
second line
This is a nonsense line
Nothing beyong this point 
'''

myfile =  open('short.txt')

line = myfile.readline()       
print(line + '...')  

line = line.rstrip()  
print(line + '...')    

# read a fe more characters fromthe file   
a_few = myfile.read(6) 
print(a_few)

rest = myfile.read()    # read the rest 
print('The rest of the file: \n' + rest)

more_data = myfile.read()  # returns empty 
print('\nMore data: ' + more_data)

myfile.close()  
