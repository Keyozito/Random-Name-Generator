import random

# Threat H as consonant, in vowel list. In order to allow formations like:
# Ash, Phill

# List Variables
cons = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vog = ['a', 'e', 'i', 'o', 'u', 'h']

# Range limit
randomNameLimit = random.randint(2,6)
randomNameString = ""

for x in range(randomNameLimit):
    if randomNameString == "":
        # First Letter
        randomNameString += random.choice(vog+cons)
    else:
        # Threat H as consonant
        if randomNameString[x-1] == 'h':
            randomNameString += random.choice(vog)
        # Vowels
        elif randomNameString[x-1] in vog:
            randomNameString += random.choice(cons)
        # Consonants
        else:
            randomNameString += random.choice(vog)

print(randomNameString)
