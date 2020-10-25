#!/usr/bin/python3
import os
import sys

if not len(sys.argv) > 1:
    t = 5
else:
    t = int(sys.argv[1])

for i in range(t):
    print(f'Screenshot {i+1} taken.')
    os.system('scrot -d 1')
