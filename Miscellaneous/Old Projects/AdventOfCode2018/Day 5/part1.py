import regex as re

print("CAUTION: Caustic Polymers Ahead!")
print("Performing Chemical Analysis...")

with open("polymer.txt") as f:
    polymer = f.read()

p = re.compile(r'[A-Z][a-z]|[a-z][A-Z]')

while True:
    matches = list(filter(lambda x: x[0].lower() == x[1].lower(), p.findall(polymer, overlapped=True)))
    if len(matches) == 0:
        break
    index = polymer.find(matches[0])
    polymer = polymer[:index] + polymer[index + 2:]

print(f"Length of Polymer: {len(polymer)}")