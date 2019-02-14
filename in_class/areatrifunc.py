def t_area(b, h):
    b = int(b)
    h = int(h)
    area = b * h * 1/2 
    return area

base  = input('Triangle Base: ')
height = input('Triangle Height: ')

triangleArea = t_area(base, height) 

print('The area of the triangle is ' +  str(triangleArea))
