with open('intcode.txt', 'r') as f:
    intcode = f.read().split(',')

intcode = list(map(int, intcode))

for a in range(101):
    for b in range(101):
        copy = [i for i in intcode]
        copy[1] = a
        copy[2] = b

        for i in range(len(copy) // 4):
            curr = copy[i*4: i*4+4]
            if curr[0] == 99:
                break
            elif curr[0] == 1:
                copy[curr[3]] = copy[curr[1]] + copy[curr[2]]
            elif curr[0] == 2:
                copy[curr[3]] = copy[curr[1]] * copy[curr[2]]

        if copy[0] == 19690720:
            print(f'{a} {b} {copy[0]}')
            print(100 * a + b)
