from itertools import combinations

with open('boxids.txt') as f:
    ids = f.read().split('\n')

def common_substring(string1, string2):
    difference = 0

    for x, y in zip(string1, string2):
        if x != y:
            difference += 1
    return difference

def find_common_substring(string1, string2):
    similar = ''
    for x, y in zip(string1, string2):
        if x == y:
            similar += x
    return similar

for x, y in combinations(ids, 2):
    if common_substring(x, y) == 1:
        break

print(find_common_substring(x, y))