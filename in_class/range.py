# testing range()

print('range(3)')
#it'll output 0 1 and 2

for i in range(3):      # from 0 to 2 
    #
    print(str(i))
    
print('range(0)')
#excludes last number??
for i in range(0):
    print(str(i))    

#2 to 10, in steps of 2 excluding 10??? 
print('range(2,10,2)')
for i in range(2,10,2):
    print(str(i))      

#from -2 to -10, exclude -10, going by steps of -2
#output: -2 -4 -6 -8, stops there... 
print('range(-2, -10, -2)')  
for i in range(-2, -10, -2):
    print(i)
    
