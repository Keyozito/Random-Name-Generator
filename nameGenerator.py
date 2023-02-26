import random
cons = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vog = ['a', 'e', 'i', 'o', 'u', 'h']

randomNameLimit = random.randint(2,6)
randomNameString = ""

for x in range(randomNameLimit):
    if randomNameString == "":
        randomNameString += random.choice(vog+cons)
    else:
        if randomNameString[x-1] == 'h':
            randomNameString += random.choice(vog)
        elif randomNameString[x-1] in vog:
            randomNameString += random.choice(cons)
        else:
            randomNameString += random.choice(vog)

print(randomNameString)
