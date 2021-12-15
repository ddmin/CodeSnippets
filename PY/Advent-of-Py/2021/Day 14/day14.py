def read_input():
    with open("day14.txt", "r") as f:
        file = list(filter(lambda x: x, f.read().split('\n')))

        polymer = file[0]
        insertions = file[1:]

    dictionary = {}
    for insertion in insertions:
        ins = insertion.split(' -> ')
        dictionary[ins[0]] = ins[1]

    return polymer, dictionary

def polymerize(polymer, insertion_rules, steps):
    pairs_count = {}
    for i in zip(polymer, polymer[1:]):
        if i not in pairs_count:
            pairs_count[i] = 0
        pairs_count[i] += 1

    new_count = {}
    for _ in range(0, steps):
        for pair in pairs_count:
            a, b = pair
            c = insertion_rules[a+b]
            if (a, c) not in new_count:
                new_count[(a, c)] = 0
            new_count[(a, c)] += pairs_count[pair]

            if (c, b) not in new_count:
                new_count[(c, b)] = 0
            new_count[(c, b)] += pairs_count[pair]

        pairs_count = new_count.copy()

    letter_count ={}
    for (a, b) in pairs_count:
        if a not in letter_count:
            letter_count[a] = 0
        letter_count[a] += pairs_count[(a, b)]

    last = polymer[-1]
    if last not in letter_count:
        letter_count[last] = 0
    letter_count[last] += 1

    vals = sorted(letter_count.values())
    return vals[-1] - vals[0]

def main():
    polymer, insertion_rules = read_input()
    ans = polymerize(polymer, insertion_rules, 40)
    print("Got:", ans)
    assert ans == 4807056953866, "WRONG ANSWER"
    print('Nice')

if __name__ == '__main__':
    main()
