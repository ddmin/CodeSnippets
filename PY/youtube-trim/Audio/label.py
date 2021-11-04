import re
import subprocess
import os
from os.path import exists

ARTDIR="./Art"
SONGDIR="./Music"
PROCDIR="./proc"

if not exists(PROCDIR):
    os.mkdir(PROCDIR)

for file in os.listdir(SONGDIR):

    album = re.search("\[(.*)\]", file).group(1)

    if exists(f'./Art/{album}.jpg'):
        art = f'./Art/{album}.jpg'
    elif exists(f'./Art/{album}.png'):
        art = f'./Art/{album}.png'
    else:
        art = 'Art/default.jpg'

    subprocess.run(
        [
            'ffmpeg',
            '-y',
            '-i', f'{SONGDIR}/{file}',
            '-c', 'copy',
            '-metadata', f'album={album}',
            f'{file}.mp3',
        ]
    )

    subprocess.run(
        [
            'ffmpeg',
            '-i', f'{file}.mp3',
            '-i', art,
            '-map_metadata', '0',
            '-map', '0',
            '-map', '1',
            '-acodec', 'copy',
            f'{file}.mp3.mp3',
        ]
    )

    subprocess.run(['rm', f'{file}.mp3'])
    subprocess.run(['mv', f'{file}.mp3.mp3', f'{PROCDIR}/{file}'])
    print('='*60)
