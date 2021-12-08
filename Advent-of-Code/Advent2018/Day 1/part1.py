with open('frequencies.txt') as f:
    frequencies = f.read().split('\n')[:-1]

print(sum(map(int, frequencies)))
