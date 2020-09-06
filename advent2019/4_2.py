import re

def ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True

def contains_double(lst):
    lst = ''.join(list(map(str, lst)))
    matches = re.findall('33+|44+|55+|66+|77+|88+|99+', lst)
    if matches and min([len(match) for match in matches]) == 2:
        return True
    else:
        return False

i = '272091-815432'
lo, hi = map(int, i.split('-'))

s = 0

i = [list(map(int, list(str(i)))) for i in range(lo, hi+1)]

i = list(filter(ascending, i))
i = list(filter(contains_double, i))

print(len(i))
