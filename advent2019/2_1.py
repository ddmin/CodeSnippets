with open('intcode.txt', 'r') as f:
    intcode = f.read().split(',')

intcode = list(map(int, intcode))

intcode[1] = 12
intcode[2] = 2

for i in range(len(intcode) // 4):
    curr = intcode[i*4: i*4+4]
    if curr[0] == 99:
        break
    elif curr[0] == 1:
        intcode[curr[3]] = intcode[curr[1]] + intcode[curr[2]]
    elif curr[0] == 2:
        intcode[curr[3]] = intcode[curr[1]] * intcode[curr[2]]

print(intcode[0])
