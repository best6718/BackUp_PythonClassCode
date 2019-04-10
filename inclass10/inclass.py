m = {'name':'Lucia', 'age':'15'}
m['city'] = 'Alameda'

my_courses = {'Python': { 'prof':'Almudena', 'score': 90}}

my_courses['Python']
my_courses['Python']['score']

list_courses = {'Python': ['Almu',99]}
list_courses['Python'][1]

for i in my_courses:
	print(i)
	print(my_courses[i])

	
my_courses['Cryptography'] = {'prof': 'Almu', 'score': 88}

for i in my_courses:
      print(my_courses[i])
