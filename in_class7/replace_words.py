def replace_words(input_file, before, after):
    #this command should open/create a file for writing if file doesn't
    #exist
    theString = ''
    x = open(input_file)
    #this next line is not needed, cuz we'd read the entire file
    #content = input_files.read()
    for eachLine in x:
        for eachWord in eachLine
            eachWord = eachWord.replace(before, after)
        theString = theString + 
    f = open('newFile.txt', 'w')
    
    x = input_file.close()
    
