def calc(lst):
    if lst[-1] <= 0:
        return lst

    x = lst[-1] // 3 - 2
    lst.append(x)

    return calc(lst)

with open('mass.txt', 'r') as f:
    modules = f.read().split('\n')[:-1]

modules = list(map(int, modules))

fn = lambda x: x>0

s = 0
for i in range(len(modules)):
    n = calc([modules[i]])[1:]
    x = sum(list(filter(fn, n)))
    s += x

print(s)
