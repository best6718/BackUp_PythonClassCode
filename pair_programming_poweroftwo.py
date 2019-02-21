x = input()
if (x == 0):
    print(1)

if (x > 0):
    if (x == 1):
        print("2")
    if (x > 1):
        i = 1
        while(i != x):
            power = power*2
            i++
        print('2^n is ' + str(power))

#n = input('what power of 2 do u want?: ')
#r = 1
#for x in range(0, int(n)):
        #r = r*2
#print(r)
