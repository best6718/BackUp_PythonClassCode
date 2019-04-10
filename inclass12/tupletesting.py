(x,y) = (2.7, 'python')
print(x)
print(y)


#that was a tuple..

t = ('a', 'b', 'c')
print(type(t))

print(t[0])

#cannot override an element like we did in list, also can't append an element
m = tuple('python')
print(m)

m = list(m)
print(m)

###
#if you call .items() on dictionary, tuple is returned
