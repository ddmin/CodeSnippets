def findLetter(letter):
    global master
    for x in range(1, len(master[0])-1):
        if master[0][x] == letter:
            return [0, x]
    for x in range(1, len(master[14])-1):
        if master[14][x] == letter:
            return [14, x]
    for x in range(len(master)):
        if master[x][0] == letter:
            return [x, 0]
        if master[x][14] == letter:
            return [x, 14]

def findDir(x, y):
    if x == 0:
        return 'DOWN'
    if y == 0:
        return 'RIGHT'
    if x == 14:
        return 'UP'
    if y == 14:
        return 'LEFT'

def checkLetter(x, y):
    global master
    if master[x][y].isalpha():
        return True
    else:
        return False

def checkMirror(direction, x, y):
    global master
    if master[x][y] == '\\':
        if direction == 'LEFT':
            return 'UP'
        if direction == 'DOWN':
            return 'RIGHT'
        if direction == 'RIGHT':
            return 'DOWN'
        if direction == 'UP':
            return 'LEFT'
        
    elif master[x][y] == '/':
        if direction == 'LEFT':
            return 'DOWN'
        if direction == 'DOWN':
            return 'LEFT'
        if direction == 'RIGHT':
            return 'UP'
        if direction == 'UP':
            return 'RIGHT'
    else:
        return direction

def move(direction, x, y):
    if direction == 'LEFT':
        return (direction, x, y-1)
    if direction == 'RIGHT':
        return (direction, x, y+1)
    if direction == 'UP':
        return (direction, x-1, y)
    if direction == 'DOWN':
        return (direction, x+1, y)

#Get the mirrors
print('Mirror:')
lst = [input() for x in range(13)]
print('------------------------------')


master = [[char for char in x] for x in lst]

alphaListOne = [x for x in ' abcdefghijklm ']
alphaListTwo = [x for x in ' NOPQRSTUVWXYZ ']

for x in range(len(master)):
    master[x].insert(0,'ABCDEFGHIJKLM'[x])

for x in range(len(master)):
    master[x].append('nopqrstuvwxyz'[x])


master.insert(0, alphaListOne)
master.insert(14, alphaListTwo)

for x in master:
    print(' '.join(x))

print('------------------------------')


for letter in input():
    x,y = findLetter(letter)
    direction = findDir(x,y)

    while True:
        #print(master[x][y])
        direction, x, y = move(direction, x, y)
        direction = checkMirror(direction, x, y)
        if checkLetter(x, y):
            break
    print(master[x][y], end='')
