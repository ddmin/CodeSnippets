from random import randint

n = randint(2, 90)
print(n)
print()

s = [x - (n - x*(n//x)) if x - (n - x*(n//x)) != x else 0 for x in range(2,21)]
efficient = min(s)

mat4 = lambda x: str(x).rjust(2, '0')
print(list(map(mat4, range(2,21))))
print(list(map(mat4, s)))
print()

for cols, x in zip(range(20,1,-1), s[::-1]):
	if x == efficient:
		break

counter = 0
for x in range(n):
	print('X', end = '')
	counter += 1
	if counter % cols == 0:
		print()

print()
