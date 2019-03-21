import random
p = ['D', 'A']
plen = len(p)
jobs = ["set table", "doing dishes"]

for i in jobs:
    x = random.randint(0, plen-1)
    print("The person to do job: " + i + " is person: " + p[x])
