def manhattan(n):
    x, y = n
    return abs(x)+abs(y)

with open('wire.txt', 'r') as f:
    wires = f.read().split('\n')[:-1]

wires[0] = wires[0].split(',')
wires[1] = wires[1].split(',')

w1_coord = [(0, 0)]
w2_coord = [(0, 0)]

for d in wires[0]:
    direction = d[0]
    amt = int(d[1:])

    x, y = w1_coord[-1]

    if direction == 'U':
        w1_coord.extend([(x, y+i) for i in range(1, amt+1)])
    elif direction == 'D':
        w1_coord.extend([(x, y-i) for i in range(1, amt+1)])
    elif direction == 'L':
        w1_coord.extend([(x-i, y) for i in range(1, amt+1)])
    elif direction == 'R':
        w1_coord.extend([(x+i, y) for i in range(1, amt+1)])

for d in wires[1]:
    direction = d[0]
    amt = int(d[1:])

    x, y = w2_coord[-1]

    if direction == 'U':
        w2_coord.extend([(x, y+i) for i in range(1, amt+1)])
    elif direction == 'D':
        w2_coord.extend([(x, y-i) for i in range(1, amt+1)])
    elif direction == 'L':
        w2_coord.extend([(x-i, y) for i in range(1, amt+1)])
    elif direction == 'R':
        w2_coord.extend([(x+i, y) for i in range(1, amt+1)])

w1_coord.remove((0, 0))
w2_coord.remove((0, 0))

sorted(w1_coord, key=manhattan)
sorted(w2_coord, key=manhattan)

for i in w1_coord:
    if i in w2_coord:
        print(manhattan(i))
        break
