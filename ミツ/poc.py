# proof of concept
import random
import time

LEET = {
        'a': '@&4',
        'b': '68',
        'c': '(',
        'd': '6)',
        'e': '3=',
        'g': '9',
        'i': '!1',
        'k': '<>',
        'l': '!12',
        'n': '^',
        'o': '0',
        'p': '?',
        'q': '9@',
        's': '5$',
        't': '7+',
        }

with open('sources/nouns.txt', 'r') as f:
    nouns = f.read().split('\n')

with open('sources/adjectives.txt', 'r') as f:
    adjs = f.read().split('\n')

with open('sources/verbs.txt', 'r') as f:
    verbs = f.read().split('\n')

ad_verbs = adjs + verbs

with open('sources/places.txt', 'r') as f:
    places = f.read().split('\n')

noun = random.choice(nouns)
ad_verb = random.choice(ad_verbs)
place = random.choice(places)

password = [noun[:min(len(noun), random.randint(4, 6))], ad_verb[:min(len(noun), random.randint(4, 6))], place[:min(len(noun), random.randint(6, 8))]]
random.shuffle(password)

password = ''.join(password).lower()
password = list(filter(lambda x: x.isalpha(), list(password)))

for i in range(2, 4):
    index = random.randint(0, len(password)-1)
    while not password[index].isalpha() or not password[index] in LEET:
        index = random.randint(0, len(password)-1)

    password[index] = random.choice(LEET[password[index]])

password = ''.join(password)

print(password)
print(f'Length: {len(password)}')
print(f'Hint: {ad_verb} {noun} at {place}')
