# [Easy] Challenge 6

import os
import math
import time

a = 1
n = 1
s = 0
i = 0

while True:
    i += 1
    os.system('clear')
    print(f'Current Iteration: {i}')
    print(f'Current Prediction: {s}')
    print(f'Error: {abs(math.pi - s)}')
    time.sleep(0.01)
    s += n * (4 / a)
    a += 2
    n *= -1
