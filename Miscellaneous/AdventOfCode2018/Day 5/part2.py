import regex as re
import string

print("CAUTION: Caustic Polymers Ahead!")
print("Performing Chemical Analysis...")
print()

with open("polymer.txt") as f:
    polymer = f.read()

def calculatePolymerLength(polymer):
    p = re.compile(r'[A-Z][a-z]|[a-z][A-Z]')

    while True:
        matches = list(filter(lambda x: x[0].lower() == x[1].lower(), p.findall(polymer, overlapped=True)))
        if len(matches) == 0:
            break
        index = polymer.find(matches[0])
        polymer = polymer[:index] + polymer[index + 2:]
    return len(polymer)

most_efficient = 0
for letter in string.ascii_lowercase:
    print(f'Removing letter "{letter.upper()}"')
    new_polymer = re.sub(letter, '', polymer)
    new_polymer = re.sub(letter.upper(), '', new_polymer)
    length = calculatePolymerLength(new_polymer)
    print(length)

    if length < most_efficient:
        most_efficient = length

print(f'Most efficient: {length}')