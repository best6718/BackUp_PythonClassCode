import random

# Family members
names = ['Dylan', 'Brandon', 'Jefferson','Michael', 'Dani']
l = len(names)
dishes = dict()

for i in names:
    dishes[i] = 0

# Who does the dishes?
answer = input("Do you want a job assignment? ")

while(answer == 'yes' or answer == 'y'):
    random_index = random.randint(0, l-1)

    random_person = names[random_index]

    dishes[random_person] += 1
    print("This is the dishes dictionary: ")
    print(dishes)
    answer = input("Do you want a job assignment? ")

print(dishes)


