data = [list(map(int, i.split(', '))) for i in open('coordinates.txt').readlines()]

# print(data)
print(*data)
# max_x = list(zip(*data))[0]
# print(max_x)