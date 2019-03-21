# Count the frequency of each word in a text   
myfile =  open('readme.txt')
myString = myfile.read()

myList = myString.split()
#myList is now an array of split strings from whatever was in the fackin file

freq = []           #keeps track of repetition
my_new_list = []   # keeps words without repetition 

#read each element of myList w/ a for loop
#each element, count how many times this word appears in my list
#create new array with first word
for word in myList:
    if word in my_new_list:
        num = myList.count(word)
        freq.append(num)
        my_new_list.append(word)

print("myList\n" + str(myList) + "\n")
print("freq\n" + str(freq) + "\n")

# printing words and frequency together 
i = 0    
for word in my_new_list:
    print(word, ' ', freq[i])
    i += 1

myfile.close() 

