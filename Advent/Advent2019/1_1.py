calc = lambda x: (int(x) // 3) - 2

with open('mass.txt', 'r') as f:
    modules = f.read().split('\n')[:-1]

result = sum(list(map(calc, modules)))
print(result)
