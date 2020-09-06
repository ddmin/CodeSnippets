i = '272091-815432'
lo, hi = map(int, i.split('-'))

s = 0
for i in range(lo, hi+1):
    ascending = True
    double = False

    n = list(map(int, list(str(i))))

    for a in range(5):
        if n[a] > n[a+1]:
            ascending = False

        if n[a] == n[a+1]:
            double = True

    if ascending and double:
        s += 1

print(s)
