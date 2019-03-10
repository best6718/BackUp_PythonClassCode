# Creates a new file if it does not exist
# Re-writes the file if it exist

myfile =  open('my.txt', 'w')
#line = ''

for c in range(1,4):
	p = input('Enter content: \n')
	#line += p + '\n'
	#same thing as
	#line = line + p + '\n'
			
myfile.write(line)	
myfile.close() 
