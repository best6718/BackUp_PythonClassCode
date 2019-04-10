my_courses = {'Python':'Almudena', 'Java': 'Barbara'}


print(my_courses['Python'])

#for loop
for i in my_courses:
    print('i:', i, 'my_courses[i]', my_courses[i])

my_courses = {'Python': {'prof': 'Almudena', 'score': 99}, 'Java': {'prof':'xxx', 'score': 88}}

for i in my_courses:
    s = ' '
    for j in my_courses[i]:
        
