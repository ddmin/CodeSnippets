def cover_fabric(xpos, ypos, xsize, ysize):
    for y in range(ysize):
        for x in range(xsize):
            fabric[ypos + y][xpos + x] += 1

def isOverlap(xpos, ypos, xsize, ysize):
    for y in range(ysize):
        for x in range(xsize):
            if fabric[ypos + y][xpos + x] != 1:
                return True
    return False

with open('claims.txt') as f:
    claims = f.read().split('\n')[:-1]

claims = [[claim.split()[0]] + claim.split()[2:] for claim in claims]
fabric = [[0 for y in range(1000)] for x in range(1000)]

for index in range(len(claims)):
    ID, position, size = claims[index]
    position = position[:-1]

    xpos, ypos = position.split(',')
    xpos = int(xpos)
    ypos = int(ypos)
    xsize, ysize = size.split('x')
    xsize = int(xsize)
    ysize = int(ysize)

    cover_fabric(xpos, ypos, xsize, ysize)

for index in range(len(claims)):
    ID, position, size = claims[index]
    position = position[:-1]

    xpos, ypos = position.split(',')
    xpos = int(xpos)
    ypos = int(ypos)
    xsize, ysize = size.split('x')
    xsize = int(xsize)
    ysize = int(ysize)

    if not(isOverlap(xpos, ypos, xsize, ysize)):
        print(ID)
