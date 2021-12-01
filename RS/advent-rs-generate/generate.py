with open('template.rs', 'r') as f:
    file = f.read()

for i in range(1, 26):
    d = str(i).zfill(2)
    with open(f'day{d}.rs', 'w') as f:
        copy = ''.join([i for i in file])
        copy = copy.replace('@', d)
        f.write(copy)
