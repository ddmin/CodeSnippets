# [Hard] Challenge 4

# 4, 2, 8
# 6, 2, 12
# 6, 2, 3
# 9, 12, 108
# 4, 16, 64

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

def remove_duplicate(lst):
    copy = []
    for n in range(len(lst) - 1):
        if not (lst[n] in lst[n+1:]):
            copy.append(lst[n])
    copy.append(lst[-1])
    return copy

def main():
    inp = remove_duplicate(input('>> ').replace(' ','').split(','))
    print()

    for op, symb in zip([add, sub, mul, div], ['+', '-', '*', '/']):
        for i in range(len(inp)):
            for n in range(i+1, len(inp)):
                print(f'{inp[i]} {symb} {inp[n]} = {op(int(inp[i]),int(inp[n]))} ')
        if symb != '/':
            print()

if __name__ == '__main__':
    main()
