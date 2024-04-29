from itertools import cycle

with open('frequencies.txt') as f:
    frequencies = f.read().split('\n')[:-1]

start = 0
already_seen = set([0])

for frequency in cycle(frequencies):
    start += int(frequency)
    if start in already_seen:
        break
    already_seen.add(start)

print(start)
