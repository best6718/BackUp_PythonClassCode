"""
Karena Huang
CS80K Python
3/13/19
replace_words.py
"""
def replace_words(input_file, before, after):
    
    f = open('newFile.txt', 'w')
    x = open(input_file)
   

    for eachLine in x:
        #some test code
        #theString = ''
        
        if(before in eachLine):
            newLine = eachLine.replace(before, after)
            #theString = theString + newLine
            
            f.write(newLine)
        else:
            f.write(eachLine)

        
    x.close()
    f.close()

replace_words('readme.txt', 'unicorn', 'DRAGONS')
    
  
    
