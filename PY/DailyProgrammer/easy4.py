# [Easy] Challenge 4

import random
import string

print('How many passwords?')
n = int(input('> '))
print()

print("Length of password(s):")
l = int(input('> '))
print()

print("Generating Passwords...")

lst = []
for a in range(n):
    passwd = ''
    for b in range(l):
        passwd += random.choice(string.ascii_letters + string.digits + string.punctuation)
    lst.append(passwd)

print('\n'.join(lst))
