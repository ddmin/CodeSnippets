with open('boxids.txt') as f:
    ids = f.read().split('\n')

twos = 0

for id in ids:
    for letter in id:
        if id.count(letter) == 2:
            twos += 1
            break

threes = 0

for id in ids:
    for letter in id:
        if id.count(letter) == 3:
            threes += 1
            break

print(twos * threes)