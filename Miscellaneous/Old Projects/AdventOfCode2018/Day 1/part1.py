with open('frequencies.txt') as f:
    frequencies = f.read().split('\n')

print(sum(map(int, frequencies)))