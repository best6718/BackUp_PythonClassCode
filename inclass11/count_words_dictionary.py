# Counting letters in a word
# See textbook
word = 'brontosaurus'
d = dict()
for c in word:
  if c not in d:
    d[c] = 1
    #at the end, dictionary has letter and frequency of it
  else:
    d[c] += 1
print('Counting letters in ', word ,d)    

# Counting the words in a sentence 
counts = dict()  
myString = "I think Python is fun. I believe Python is powerful."

# words is a list
words = myString.split() 

for word in words:  
  if word not in counts:  
    counts[word]= 1  
  else:  
    counts[word] +=  1  

print('\ncounts: ', counts)

# Advance practice 
# An easier faster way to count occurence in a list
my_new = dict()  
for word in words:  
  my_new[word] = my_new.get(word,0) + 1  
print('\ncounts: ', my_new) 

# Note: get returns 0 if the word is not found as a key in my_new 
# if the word is in my_new then it returns the value of word  
